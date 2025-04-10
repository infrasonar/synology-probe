from asyncsnmplib.mib.mib_index import MIB_INDEX
from libprobe.asset import Asset
from ..snmpclient import get_snmp_client
from ..snmpquery import snmpquery

QUERIES = (
    MIB_INDEX['SYNOLOGY-SERVICES-MIB']['serviceEntry'],
)


async def check_service(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:

    snmp = get_snmp_client(asset, asset_config, check_config)
    state = await snmpquery(snmp, QUERIES)
    for item in state.get('serviceEntry', []):
        item['name'] = item.pop('serviceName')
        item.pop('serviceInfoIndex', None)
    return state
