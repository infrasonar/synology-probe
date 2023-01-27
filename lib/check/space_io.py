from asyncsnmplib.mib.mib_index import MIB_INDEX
from libprobe.asset import Asset
from ..utils import get_data

QUERIES = (
    MIB_INDEX['SYNOLOGY-SPACEIO-MIB']['spaceIOEntry'],
)


async def check_space_io(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:

    state = await get_data(asset, asset_config, check_config, QUERIES)
    for item in state.get('spaceIOEntry', []):
        item['name'] = item.pop('spaceIODevice')
        item.pop('spaceIOIndex')
    return state
