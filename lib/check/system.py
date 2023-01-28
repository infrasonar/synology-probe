from asyncsnmplib.mib.mib_index import MIB_INDEX
from libprobe.asset import Asset
from libprobe.exceptions import CheckException
from ..utils import get_data

QUERIES = (
    MIB_INDEX['SYNOLOGY-SYSTEM-MIB']['synoSystem'],
    MIB_INDEX['SYNOLOGY-SYSTEM-MIB']['dsmInfo'],
    MIB_INDEX['SYNOLOGY-SYSTEM-MIB']['fan'],
)

STATUS = {
    1: 'Normal',
    2: 'Failed',
}

UPGRADE = {
    1: 'Available',
    2: 'Unavailable',
    3: 'Connecting',
    4: 'Disconnected',
    5: 'Others',
}


async def check_system(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:

    state = await get_data(asset, asset_config, check_config, QUERIES)
    try:
        system = state['synoSystem'][0]
        fan = state['fan'][0]
        dsm_info = state['dsmInfo'][0]
    except Exception:
        raise CheckException('incomplete data')

    return {
        'system': {
            'name': 'system',
            'systemStatus': STATUS.get(system.get('systemStatus')),
            'temperature': system.get('temperature'),
            'powerStatus': STATUS.get(system.get('powerStatus')),
            'controllerNumber': system.get('controllerNumber'),
            'systemFanStatus': STATUS.get(fan.get('systemFanStatus')),
            'cpuFanStatus': STATUS.get(fan.get('cpuFanStatus')),
            'modelName': dsm_info.get('modelName'),
            'serialNumber': dsm_info.get('serialNumber'),
            'version': dsm_info.get('version'),
            'upgradeAvailable': UPGRADE.get(dsm_info.get('upgradeAvailable')),
        }
    }
