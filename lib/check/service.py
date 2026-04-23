from asyncsnmplib.mib.mib_index import MIB_INDEX
from libprobe.asset import Asset
from libprobe.check import Check
from ..snmpclient import get_snmp_client
from ..snmpquery import snmpquery

QUERIES = (
    (MIB_INDEX['SYNOLOGY-SERVICES-MIB']['serviceEntry'], True),
)


class CheckService(Check):
    key = 'service'
    unchanged_eol = 0

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        snmp = get_snmp_client(asset, local_config, config)
        state = await snmpquery(snmp, QUERIES)
        for item in state.get('serviceEntry', []):
            item['name'] = item.pop('serviceName')
            item.pop('serviceInfoIndex', None)
        return state
