from asyncsnmplib.mib.mib_index import MIB_INDEX
from libprobe.asset import Asset
from ..utils import get_data

QUERIES = (
    MIB_INDEX['SYNOLOGY-SYSTEM-MIB']['synoSystem'],
    MIB_INDEX['SYNOLOGY-SYSTEM-MIB']['dsmInfo'],
    MIB_INDEX['SYNOLOGY-SYSTEM-MIB']['fan'],
)


async def check_system(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:

    state = await get_data(asset, asset_config, check_config, QUERIES)
    return state
