from libprobe.probe import Probe
from lib.check.disk import CheckDisk
from lib.check.disk_smart import CheckDiskSMART
from lib.check.ebox import CheckEbox
from lib.check.iscsi_lun import CheckISCSILUN
from lib.check.raid import CheckRaid
from lib.check.service import CheckService
from lib.check.space_io import CheckSpaceIO
from lib.check.storage_io import CheckStorageIO
from lib.check.system import CheckSystem
from lib.version import __version__ as version


if __name__ == '__main__':
    checks = (
        CheckDisk,
        CheckDiskSMART,
        CheckEbox,
        CheckISCSILUN,
        CheckRaid,
        CheckService,
        CheckSpaceIO,
        CheckStorageIO,
        CheckSystem,
    )

    probe = Probe("synology", version, checks)

    probe.start()
