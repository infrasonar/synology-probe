from asyncsnmplib.mib.mib_index import MIB_INDEX
from libprobe.asset import Asset
from libprobe.check import Check
from ..snmpclient import get_snmp_client
from ..snmpquery import snmpquery

QUERIES = (
    (MIB_INDEX['SYNOLOGY-SPACEIO-MIB']['spaceIOEntry'], True),
)


class CheckSpaceIO(Check):
    key = 'spaceIO'
    unchanged_eol = 0

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        snmp = get_snmp_client(asset, local_config, config)
        state = await snmpquery(snmp, QUERIES)
        for item in state.get('spaceIOEntry', []):
            item['name'] = item.pop('spaceIODevice')
            item.pop('spaceIOIndex', None)
        return state
