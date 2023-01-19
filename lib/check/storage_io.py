from asyncsnmplib.mib.mib_index import MIB_INDEX
from libprobe.asset import Asset
from ..snmpquery import snmpquery

QUERIES = (
    MIB_INDEX['SYNOLOGY-STORAGEIO-MIB']['storageIOEntry'],
)


async def check_storage_io(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:

    state = await snmpquery(asset, asset_config, check_config, QUERIES)
    for item in state.get('storageIO', []):
        item['name'] = item.pop('Device')
        item.pop('Index')
    return state
