from asyncsnmplib.mib.mib_index import MIB_INDEX
from libprobe.asset import Asset
from libprobe.exceptions import IgnoreCheckException
from ..utils import get_data

QUERIES = (
    MIB_INDEX['SYNOLOGY-EBOX-MIB']['eboxEntry'],
)


async def check_ebox(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:

    state = await get_data(asset, asset_config, check_config, QUERIES)

    ebox = state.get('eboxEntry')
    if not ebox:
        raise IgnoreCheckException

    return state
