import logging
from datetime import datetime, timedelta

from zino.config.models import PollDevice
from zino.scheduler import get_scheduler
from zino.snmp import SNMP
from zino.tasks.task import Task

_logger = logging.getLogger(__name__)


class ReachableTask(Task):
    EXTRA_JOBS_PREFIX = "delayed_reachable_job"
    EXTRA_JOBS_INTERVALS = [60, 120, 240, 480, 960]

    def __init__(self):
        self._scheduler = get_scheduler()

    async def run(self, device: PollDevice):
        """Checks if device is reachable. Schedules extra jobs if not."""
        snmp = SNMP(device)
        result = await snmp.get("SNMPv2-MIB", "sysUpTime", 0)
        if not result:
            _logger.debug("Device %s is not reachable", device.name)
            if not self.extra_jobs_are_running():
                self.schedule_extra_jobs(device)
        else:
            _logger.debug("Device %s is reachable", device.name)
            if self.extra_jobs_are_running():
                self.deschedule_extra_jobs()

    def schedule_extra_jobs(self, device: PollDevice):
        for interval in self.EXTRA_JOBS_INTERVALS:
            name = self.get_job_name_for_interval(interval, device)
            run_date = datetime.now() + timedelta(seconds=interval)
            self._scheduler.add_job(
                self.task,
                "date",
                run_date=run_date,
                args=(device,),
                name=name,
                id=name,
            )

    def deschedule_extra_jobs(self, device: PollDevice):
        for interval in self.EXTRA_JOBS_INTERVALS:
            name = self.get_job_name_for_interval(interval, device)
            self._scheduler.remove_job(name)

    def extra_jobs_are_running(self, device: PollDevice):
        for interval in self.EXTRA_JOBS_INTERVALS:
            job_name = self.get_job_name_for_interval(interval, device)
            if self._scheduler.get_job(job_name):
                return True
        return False

    def get_job_name_for_interval(self, interval, device):
        return f"{self.EXTRA_JOBS_PREFIX}_{interval}_{device.name}"
