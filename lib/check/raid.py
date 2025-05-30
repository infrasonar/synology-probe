from asyncsnmplib.mib.mib_index import MIB_INDEX
from libprobe.asset import Asset
from ..snmpclient import get_snmp_client
from ..snmpquery import snmpquery

QUERIES = (
    (MIB_INDEX['SYNOLOGY-RAID-MIB']['raidEntry'], True),
)

RAID_STATUS = {
    None: None,
    1: 'Normal',
    2: 'Repairing',
    3: 'Migrating',
    4: 'Expanding',
    5: 'Deleting',
    6: 'Creating',
    7: 'RaidSyncing',
    8: 'RaidParityChecking',
    9: 'RaidAssembling',
    10: 'Canceling',
    11: 'Degrade',
    12: 'Crashed',
    13: 'DataScrubbing',
    14: 'RaidDeploying',
    15: 'RaidUnDeploying',
    16: 'RaidMountCache',
    17: 'RaidUnmountCache',
    18: 'RaidExpandingUnfinishedSHR',
    19: 'RaidConvertSHRToPool',
    20: 'RaidMigrateSHR1ToSHR2',
    21: 'RaidUnknownStatus',
}


async def check_raid(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:

    snmp = get_snmp_client(asset, asset_config, check_config)
    state = await snmpquery(snmp, QUERIES)
    for item in state.get('raidEntry', []):
        item['name'] = item.pop('raidName')
        item['raidStatus'] = RAID_STATUS.get(item.get('raidStatus'))
        item.pop('raidIndex', None)
    return state
