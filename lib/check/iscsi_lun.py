from asyncsnmplib.mib.mib_index import MIB_INDEX
from libprobe.asset import Asset
from libprobe.exceptions import IgnoreCheckException
from ..snmpclient import get_snmp_client
from ..snmpquery import snmpquery

QUERIES = (
    MIB_INDEX['SYNOLOGY-ISCSILUN-MIB']['iSCSILUNEntry'],
)


async def check_iscsi_lun(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:

    snmp = get_snmp_client(asset, asset_config, check_config)
    state = await snmpquery(snmp, QUERIES)

    iscsi_lun = state.get('iSCSILUNEntry')
    if not iscsi_lun:
        raise IgnoreCheckException

    for item in iscsi_lun:
        item['name'] = item.pop('iSCSILUNName')
        item.pop('iSCSILUNIndex', None)
    return state
