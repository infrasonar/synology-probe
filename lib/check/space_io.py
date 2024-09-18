from asyncsnmplib.mib.mib_index import MIB_INDEX
from libprobe.asset import Asset
from ..snmpclient import get_snmp_client
from ..snmpquery import snmpquery

QUERIES = (
    MIB_INDEX['SYNOLOGY-SPACEIO-MIB']['spaceIOEntry'],
)


async def check_space_io(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:

    snmp = get_snmp_client(asset, asset_config, check_config)
    state = await snmpquery(snmp, QUERIES)
    for item in state.get('spaceIOEntry', []):
        item['name'] = item.pop('spaceIODevice')
        item.pop('spaceIOIndex', None)
    return state
