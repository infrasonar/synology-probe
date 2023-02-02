from asyncsnmplib.mib.mib_index import MIB_INDEX
from libprobe.asset import Asset
from ..utils import get_data

QUERIES = (
    MIB_INDEX['SYNOLOGY-DISK-MIB']['diskEntry'],
)

DISK_STATUS = {
    1: 'Normal',
    2: 'Initialized',
    3: 'NotInitialized',
    4: 'SystemPartitionFailed',
    5: 'Crashed',
}

DISK_HEALTH_STATUS = {
    1: 'Normal',
    2: 'Warning',
    3: 'Critical',
    4: 'Failing',
}


async def check_disk(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:

    state = await get_data(asset, asset_config, check_config, QUERIES)
    for item in state.get('diskEntry', []):
        item['name'] = item.pop('diskID')
        item['diskStatus'] = DISK_STATUS.get(item.get('diskStatus'))
        item['diskHealthStatus'] = DISK_HEALTH_STATUS.get(
            item.get('diskHealthStatus'))
        item.pop('diskIndex', None)
    return state
