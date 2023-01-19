from asyncsnmplib.mib.mib_index import MIB_INDEX
from libprobe.asset import Asset
from libprobe.exceptions import IgnoreCheckException
from ..snmpquery import snmpquery

QUERIES = (
    MIB_INDEX['SYNOLOGY-ISCSILUN-MIB']['iSCSILUNEntry'],
)


async def check_iscsi_lun(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:

    state = await snmpquery(asset, asset_config, check_config, QUERIES)

    iscsi_lun = state.get('iSCSILUN')
    if not iscsi_lun:
        raise IgnoreCheckException

    for item in iscsi_lun:
        item['name'] = item.pop('Name')
        item.pop('Index')
    return state
