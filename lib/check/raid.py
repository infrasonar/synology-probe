from asyncsnmplib.mib.mib_index import MIB_INDEX
from libprobe.asset import Asset
from ..snmpquery import snmpquery

QUERIES = (
    MIB_INDEX['SYNOLOGY-RAID-MIB']['raidEntry'],
)

# we need to patch the mib because and IMPORT is missing
for oid in (
    MIB_INDEX['SYNOLOGY-RAID-MIB']['raidFreeSize'],
    MIB_INDEX['SYNOLOGY-RAID-MIB']['raidTotalSize']
):
    MIB_INDEX[oid]['syntax']['tp'] = 'INTEGER'


async def check_raid(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:

    state = await snmpquery(asset, asset_config, check_config, QUERIES)
    for item in state.get('raid', []):
        item['name'] = item.pop('Name')
        item.pop('Index')
    return state
