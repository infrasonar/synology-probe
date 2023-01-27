from asyncsnmplib.mib.mib_index import MIB_INDEX
from libprobe.asset import Asset
from ..utils import get_data

QUERIES = (
    MIB_INDEX['SYNOLOGY-DISK-MIB']['diskEntry'],
)


async def check_disk(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:

    state = await get_data(asset, asset_config, check_config, QUERIES)
    for item in state.get('diskEntry', []):
        item['name'] = item.pop('diskID')
        item.pop('diskIndex')
    return state
