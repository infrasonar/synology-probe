from asyncsnmplib.mib.mib_index import MIB_INDEX
from libprobe.asset import Asset
from libprobe.exceptions import IgnoreCheckException
from ..utils import get_data

QUERIES = (
    MIB_INDEX['SYNOLOGY-ISCSILUN-MIB']['iSCSILUNEntry'],
)


async def check_iscsi_lun(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:

    state = await get_data(asset, asset_config, check_config, QUERIES)

    iscsi_lun = state.get('iSCSILUNEntry')
    if not iscsi_lun:
        raise IgnoreCheckException

    for item in iscsi_lun:
        item['name'] = item.pop('iSCSILUNName')
        item.pop('iSCSILUNIndex', None)
    return state
