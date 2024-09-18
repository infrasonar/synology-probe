from asyncsnmplib.mib.mib_index import MIB_INDEX
from libprobe.asset import Asset
from ..snmpclient import get_snmp_client
from ..snmpquery import snmpquery

QUERIES = (
    MIB_INDEX['SYNOLOGY-DISK-MIB']['diskEntry'],
)

DISK_STATUS = {
    None: None,
    1: 'Normal',
    2: 'Initialized',
    3: 'NotInitialized',
    4: 'SystemPartitionFailed',
    5: 'Crashed',
}

DISK_HEALTH_STATUS = {
    None: None,
    1: 'Normal',
    2: 'Warning',
    3: 'Critical',
    4: 'Failing',
}


async def check_disk(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:

    snmp = get_snmp_client(asset, asset_config, check_config)
    state = await snmpquery(snmp, QUERIES)
    for item in state.get('diskEntry', []):
        item['name'] = item.pop('diskID')
        item['diskStatus'] = DISK_STATUS.get(item.get('diskStatus'))
        item['diskHealthStatus'] = DISK_HEALTH_STATUS.get(
            item.get('diskHealthStatus'))
        item.pop('diskIndex', None)
    return state
