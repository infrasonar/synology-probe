from libprobe.probe import Probe
from lib.check.synology import check_synology
from lib.version import __version__ as version


if __name__ == '__main__':
    checks = {
        'synology': check_synology
    }

    probe = Probe("synology", version, checks)

    probe.start()
