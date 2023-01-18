from libprobe.probe import Probe
from lib.check.system import check_system
from lib.check.disk import check_disk
from lib.check.raid import check_raid
from lib.version import __version__ as version


if __name__ == '__main__':
    checks = {
        'disk': check_disk,
        'raid': check_raid,
        'system': check_system,
    }

    probe = Probe("synology", version, checks)

    probe.start()
