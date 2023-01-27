from asyncsnmplib.mib.mib_index import MIB_INDEX
from libprobe.asset import Asset
from ..utils import get_data

QUERIES = (
    MIB_INDEX['SYNOLOGY-SERVICES-MIB']['serviceEntry'],
)


async def check_service(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:

    state = await get_data(asset, asset_config, check_config, QUERIES)
    for item in state.get('serviceEntry', []):
        item['name'] = item.pop('serviceName')
        item.pop('serviceInfoIndex')
    return state
