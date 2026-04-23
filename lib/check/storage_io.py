from asyncsnmplib.mib.mib_index import MIB_INDEX
from libprobe.asset import Asset
from libprobe.check import Check
from ..snmpclient import get_snmp_client
from ..snmpquery import snmpquery

QUERIES = (
    (MIB_INDEX['SYNOLOGY-STORAGEIO-MIB']['storageIOEntry'], True),
)


class CheckStorageIO(Check):
    key = 'storageIO'
    unchanged_eol = 0

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        snmp = get_snmp_client(asset, local_config, config)
        state = await snmpquery(snmp, QUERIES)
        for item in state.get('storageIOEntry', []):
            item['name'] = item.pop('storageIODevice')
            item.pop('storageIOIndex', None)
        return state
