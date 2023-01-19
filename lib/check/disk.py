from asyncsnmplib.mib.mib_index import MIB_INDEX
from libprobe.asset import Asset
from ..snmpquery import snmpquery

QUERIES = (
    MIB_INDEX['SYNOLOGY-DISK-MIB']['diskEntry'],
)


async def check_disk(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:

    state = await snmpquery(asset, asset_config, check_config, QUERIES)
    for item in state.get('disk', []):
        item['name'] = item.pop('ID')
        item.pop('Index')
    return state
