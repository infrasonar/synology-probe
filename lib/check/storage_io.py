from asyncsnmplib.mib.mib_index import MIB_INDEX
from libprobe.asset import Asset
from ..snmpclient import get_snmp_client
from ..snmpquery import snmpquery

QUERIES = (
    MIB_INDEX['SYNOLOGY-STORAGEIO-MIB']['storageIOEntry'],
)


async def check_storage_io(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:

    snmp = get_snmp_client(asset, asset_config, check_config)
    state = await snmpquery(snmp, QUERIES)
    for item in state.get('storageIOEntry', []):
        item['name'] = item.pop('storageIODevice')
        item.pop('storageIOIndex', None)
    return state
