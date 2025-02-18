"""Basic data models for keeping/serializing/deserializing Zino state"""
import datetime
import logging
from enum import Enum
from ipaddress import IPv4Address, IPv6Address
from typing import Any, Dict, List, Literal, Optional, Union

from pydantic import BaseModel, Field

from zino.compat import StrEnum
from zino.time import now

IPAddress = Union[IPv4Address, IPv6Address]
AlarmType = Literal["yellow", "red"]
PortOrIPAddress = Union[int, IPAddress, AlarmType]

_logger = logging.getLogger(__name__)


class InterfaceState(StrEnum):
    """Enumerates allowable interface states.  Most of these values come from ifOperState from RFC 2863 (IF-MIB), but
    also adds internal Zino states that don't exist in the MIB.
    """

    ADMIN_DOWN = "adminDown"
    UP = "up"
    DOWN = "down"
    TESTING = "testing"
    UNKNOWN = "unknown"
    DORMANT = "dormant"
    NOT_PRESENT = "notPresent"
    LOWER_LAYER_DOWN = "lowerLayerDown"


class BFDSessState(StrEnum):
    """The set of allowable BFD session states"""

    ADMIN_DOWN = "adminDown"
    DOWN = "down"
    INIT = "init"
    UP = "up"
    NO_SESSION = "noSession"
    FAILING = "failing"  # Cisco proprietary


class BFDState(BaseModel):
    """Keeps BFD state for an interface"""

    session_state: BFDSessState
    session_index: Optional[int] = None
    session_discr: Optional[int] = None
    session_addr: Optional[IPAddress] = None


class Port(BaseModel):
    """Keeps port state"""

    ifindex: int
    ifdescr: Optional[str] = None
    ifalias: Optional[str] = None
    state: Optional[InterfaceState] = None
    bfd_state: Optional[BFDState] = None


class DeviceState(BaseModel):
    """Keep device state"""

    name: str
    enterprise_id: Optional[int] = None
    boot_time: Optional[int] = None
    ports: Dict[int, Port] = {}
    alarms: Optional[Dict[AlarmType, int]] = None
    boot_time: Optional[datetime.datetime] = None

    # This is the remaining set of potential device attributes stored in device state by the original Zino code:
    # EventId
    # JNXalarms
    # RunsOn
    # bfdSessAddr
    # bfdSessAddrType
    # bfdSessDiscr
    # bfdSessState
    # bgpPeerAdminState
    # bgpPeerOperState
    # bgpPeerUpTime
    # bgpPeers
    # firstFlap
    # flapping
    # flaps
    # isCisco
    # isJuniper
    # lastAge
    # lastFlap
    # portState
    # portToIfDescr
    # portToLocIfDescr
    # sawPeer

    @property
    def is_cisco(self):
        return self.enterprise_id == 9

    @property
    def is_juniper(self):
        return self.enterprise_id == 2636

    def set_boot_time_from_uptime(self, uptime: int):
        """Calculates and sets the device boot time from a current uptime value.

        :param uptime: An uptime value in 100ths of a second
        """
        self.boot_time = now() - datetime.timedelta(seconds=uptime / 100)


class DeviceStates(BaseModel):
    """Keeps track of the state of all devices we have polled from"""

    devices: Dict[str, DeviceState] = {}

    def __getitem__(self, item) -> DeviceState:
        return self.devices[item]

    def __contains__(self, item):
        return item in self.devices

    def __len__(self):
        return len(self.devices)

    def get(self, device_name: str) -> DeviceState:
        """Returns a DeviceState object for device_name, creating a blank state object if none exists"""
        if device_name not in self:
            self.devices[device_name] = DeviceState(name=device_name)
        return self[device_name]


class LogEntry(BaseModel):
    """Event log entry attributes. These apply both for 'log' and 'history' lists"""

    timestamp: datetime.datetime = Field(default_factory=now)
    message: str

    def model_dump_legacy(self) -> List[str]:
        """Returns the contents of this log entry as a sequence of text lines.

        This sequence of text lines are formatted as expected in a multi-line response in the Zino legacy server
        protocol:

        The first line starts with a UNIX integer timestamp, followed by a space and then the first line of the entry
        text.  Each subsequent line of the entry text is prefixed by a space, which in the protocol signifies a
        continuation line.

        Example:
        >>> LogEntry(message="This is a\\nmulti-line entry").model_dump_legacy()
        ['1701171730 This is a', ' multiline entry']
        >>>
        """
        unix_timestamp = int(self.timestamp.timestamp())
        lines = [f" {line}" for line in self.message.splitlines()]
        lines[0] = f"{unix_timestamp}{lines[0]}"
        return lines


class EventState(Enum):
    """The set of allowable event states"""

    EMBRYONIC = "embryonic"
    OPEN = "open"
    WORKING = "working"
    WAITING = "waiting"
    CONFIRM = "confirm-wait"
    IGNORED = "ignored"
    CLOSED = "closed"


class ReachabilityState(Enum):
    """The set of allowed reachability states"""

    REACHABLE = "reachable"
    NORESPONSE = "no-response"


class Event(BaseModel):
    """Keeps track of event state"""

    id: Optional[int] = None

    router: str
    port: Optional[PortOrIPAddress] = None
    type: Literal["Event"] = "Event"
    state: EventState = EventState.EMBRYONIC
    opened: datetime.datetime = Field(default_factory=now)
    updated: Optional[datetime.datetime] = None
    priority: int = 100

    log: List[LogEntry] = []
    history: List[LogEntry] = []

    # More-or-less optional event attrs (as guesstimated from the original Zino code)
    lasttrans: Optional[datetime.datetime] = None
    flaps: Optional[int] = None
    ac_down: Optional[datetime.timedelta] = None

    polladdr: Optional[IPAddress] = None

    def set_state(self, new_state: EventState, user: str = "monitor"):
        """Sets a new event state value, logging the change to the event history with a username"""
        if new_state == self.state:
            return

        old_state, self.state = self.state, new_state
        if (old_state, new_state) == (EventState.EMBRYONIC, EventState.OPEN):
            self.opened = now()
        self.add_history(f"state change {old_state.value} -> {new_state.value} ({user})")
        _logger.debug("id %s state %s -> %s by %s", self.id, old_state.value, new_state.value, user)

    def add_log(self, message: str) -> LogEntry:
        entry = LogEntry(message=message)
        self.log.append(entry)
        self.updated = entry.timestamp
        return entry

    def add_history(self, message: str) -> LogEntry:
        entry = LogEntry(message=message)
        self.history.append(entry)
        return entry

    def model_dump_simple_attrs(self) -> dict[str, str]:
        """Serializes the "simple" attributes of this event to the text format used by the legacy Zino protocol.

        "Simple" attributes are typically "single line" public attributes, i.e. anything but `log` or `history`.

        It would be nice to be able to attach custom serializers to fields, but we need to support multiple
        serialization formats (one for JSON state dumps, one for the legacy Zino protocol), and it's not clear how
        Pydantic can support that.
        """
        attrs = self.model_dump(mode="python", exclude={"log", "history"}, exclude_none=True)
        return {attr: self.zinoify_value(value) for attr, value in attrs.items()}

    @staticmethod
    def zinoify_value(value: Any) -> str:
        """Serializes an Event value into a plain string in the format expected by the legacy Zino protocol"""
        if isinstance(value, Enum):
            return str(value.value)
        if isinstance(value, datetime.datetime):
            return str(int(value.timestamp()))
        return str(value)


class PortStateEvent(Event):
    type: Literal["portstate"] = "portstate"
    ifindex: Optional[int] = None
    portstate: Optional[InterfaceState] = None
    descr: Optional[str] = None


class BGPEvent(Event):
    type: Literal["bgp"] = "bgp"
    remote_addr: Optional[IPAddress] = None
    remote_as: Optional[int] = None
    peer_uptime: Optional[int] = None


class BFDEvent(Event):
    type: Literal["bfd"] = "bfd"
    bfdstate: Optional[BFDSessState] = None
    bfdix: Optional[int] = None
    bfddiscr: Optional[int] = None
    bfdaddr: Optional[IPAddress] = None


class ReachabilityEvent(Event):
    type: Literal["reachability"] = "reachability"
    reachability: Optional[ReachabilityState] = None


class AlarmEvent(Event):
    type: Literal["alarm"] = "alarm"
    alarm_count: Optional[int] = None
