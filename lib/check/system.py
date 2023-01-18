from asyncsnmplib.mib.mib_index import MIB_INDEX
from libprobe.asset import Asset
from ..snmpquery import snmpquery

QUERIES = (
    MIB_INDEX['SYNOLOGY-SYSTEM-MIB']['synoSystem'],
    MIB_INDEX['SYNOLOGY-SYSTEM-MIB']['dsmInfo'],
    MIB_INDEX['SYNOLOGY-SYSTEM-MIB']['fan'],
)


async def check_system(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:

    state = await snmpquery(asset, asset_config, check_config, QUERIES)
    return state
