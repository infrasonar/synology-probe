from asyncsnmplib.mib.mib_index import MIB_INDEX
from libprobe.asset import Asset
from libprobe.exceptions import IgnoreCheckException
from ..snmpquery import snmpquery

QUERIES = (
    MIB_INDEX['SYNOLOGY-EBOX-MIB']['eboxEntry'],
)


async def check_ebox(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:

    state = await snmpquery(asset, asset_config, check_config, QUERIES)

    iscsi_lun = state.get('ebox')
    if not iscsi_lun:
        raise IgnoreCheckException

    return state
