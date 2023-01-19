from asyncsnmplib.mib.mib_index import MIB_INDEX
from libprobe.asset import Asset
from ..snmpquery import snmpquery

QUERIES = (
    MIB_INDEX['SYNOLOGY-SERVICES-MIB']['serviceEntry'],
)


async def check_service(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:

    state = await snmpquery(asset, asset_config, check_config, QUERIES)
    for item in state.get('service', []):
        item['name'] = item.pop('Name')
        item.pop('InfoIndex')
    return state
