from asyncsnmplib.mib.mib_index import MIB_INDEX
from libprobe.asset import Asset
from ..utils import get_data

QUERIES = (
    MIB_INDEX['SYNOLOGY-RAID-MIB']['raidEntry'],
)


async def check_raid(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:

    state = await get_data(asset, asset_config, check_config, QUERIES)
    for item in state.get('raidEntry', []):
        item['name'] = item.pop('raidName')
        item.pop('raidIndex')
    return state
