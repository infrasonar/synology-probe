from asyncsnmplib.mib.mib_index import MIB_INDEX
from libprobe.asset import Asset
from ..utils import get_data

QUERIES = (
    MIB_INDEX['SYNOLOGY-STORAGEIO-MIB']['storageIOEntry'],
)


async def check_storage_io(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:

    state = await get_data(asset, asset_config, check_config, QUERIES)
    for item in state.get('storageIOEntry', []):
        item['name'] = item.pop('storageIODevice')
        item.pop('storageIOIndex')
    return state
