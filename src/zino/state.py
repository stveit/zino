"""This module exists to hold global state for a Zino process"""

__all__ = ["polldevs", "devices"]

import logging
import pprint
from typing import Dict

from zino.config.models import PollDevice
from zino.events import Events
from zino.statemodels import DeviceStates

_log = logging.getLogger(__name__)
STATE_FILENAME = "zino-state.json"

# Dictionary of configured devices
polldevs: Dict[str, PollDevice] = {}

# Dictionary of device state
devices = DeviceStates()

# Dictionary of ongoing events
events = Events()


async def dump_state_to_log():
    _log.debug("Dumping state to log:\n%s", pprint.pformat(events.dict(exclude_none=True)))


async def dump_state_to_file(filename: str = STATE_FILENAME):
    """Dumps the event state to a file as JSON.

    Does not dump all state (yet).

    Once the event structure gets large, this could noticeably block the main event loop while writing to disk.  It
    might therefore be better defined as a synchronous function, so that the scheduler will run it in a worker
    thread. However, that may introduce issues with thread-safety, since the data structures that are being dumped
    may be concurrently updated by another thread.
    """
    _log.debug("dumping state to %s", filename)
    with open(filename, "w") as statefile:
        statefile.write(events.json(exclude_none=True, indent=2))


def load_state_from_file(filename: str = STATE_FILENAME):
    """Loads and replaces Zino state from a JSON file dump"""
    _log.info("Loading saved state from %s", filename)
    try:
        loaded_state = Events.parse_file(filename)
    except FileNotFoundError:
        _log.error("No state file found (%s), starting from scratch ", filename)
        return
    else:
        global events
        events = loaded_state
