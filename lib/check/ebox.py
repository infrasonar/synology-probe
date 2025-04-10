from asyncsnmplib.mib.mib_index import MIB_INDEX
from libprobe.asset import Asset
from libprobe.exceptions import IgnoreCheckException
from ..snmpclient import get_snmp_client
from ..snmpquery import snmpquery

QUERIES = (
    (MIB_INDEX['SYNOLOGY-EBOX-MIB']['eboxEntry'], True),
)


async def check_ebox(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:

    snmp = get_snmp_client(asset, asset_config, check_config)
    state = await snmpquery(snmp, QUERIES)

    ebox = state.get('eboxEntry')
    if not ebox:
        raise IgnoreCheckException

    return state
