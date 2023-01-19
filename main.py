from libprobe.probe import Probe
from lib.check.disk import check_disk
from lib.check.disk_smart import check_disk_smart
from lib.check.ebox import check_ebox
from lib.check.iscsi_lun import check_iscsi_lun
from lib.check.raid import check_raid
from lib.check.service import check_service
from lib.check.space_io import check_space_io
from lib.check.storage_io import check_storage_io
from lib.check.system import check_system
from lib.version import __version__ as version


if __name__ == '__main__':
    checks = {
        'disk': check_disk,
        'diskSMART': check_disk_smart,
        'ebox': check_ebox,
        'iSCSILUN': check_iscsi_lun,
        'raid': check_raid,
        'service': check_service,
        'spaceIO': check_space_io,
        'storageIO': check_storage_io,
        'system': check_system,
    }

    probe = Probe("synology", version, checks)

    probe.start()
