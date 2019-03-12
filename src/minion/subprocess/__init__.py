from minion.subprocess.base import BaseCommand
from minion.subprocess.rsync import RsyncSubprocess
from minion.subprocess.create_group_file import CreateGroupFileCommand
from minion.subprocess.remove_path import RemovePathCommand
from minion.subprocess.create_ids_file import CreateIdsFileCommand
from minion.subprocess.dnet_recovery import DnetRecoverySubprocess
from minion.subprocess.ubic import UbicSubprocess
from minion.subprocess.dnet_client import DnetClientSubprocess
from minion.subprocess.lrc_list import LrcListSubprocess
from minion.subprocess.lrc_convert import LrcConvertSubprocess
from minion.subprocess.lrc_defrag import LrcDefragSubprocess
from minion.subprocess.lrc_validate import LrcValidateSubprocess
from minion.subprocess.mds_cleanup import MdsCleanupSubprocess
from minion.subprocess.create_group import CreateGroupCommand
from minion.subprocess.remove_group import RemoveGroupCommand
from minion.subprocess.lrc_recover import LrcRecoverSubprocess
from minion.subprocess.lrc_remove import LrcRemoveSubprocess
from minion.subprocess.move_path import MovePathCommand
from minion.subprocess.move_elliptics_data import MoveEllipticsDataCommand
from minion.subprocess.lock_backend import LockBackendCommand
from minion.subprocess.create_file_marker import CreateFileMarkerCommand
from minion.subprocess.unlock_backend import UnlockBackendCommand
from minion.subprocess.remove_group_file import RemoveGroupFileCommand
from minion.subprocess.check_file_system import CheckFileSystemCommand
from minion.subprocess.ping import PingCommand
from minion.subprocess.check_group_location import CheckGroupLocation
from minion.subprocess.eblob_kit import EblobKitSubprocess
from minion.subprocess.mds_gc import MdsGcSubprocess

__all__ = (
    RsyncSubprocess,
    DnetRecoverySubprocess,
    UbicSubprocess,
    DnetClientSubprocess,
    LrcListSubprocess,
    LrcConvertSubprocess,
    LrcDefragSubprocess,
    LrcValidateSubprocess,
    MdsCleanupSubprocess,
    LrcRecoverSubprocess,
    LrcRemoveSubprocess,
    EblobKitSubprocess,
    MdsGcSubprocess,

    CreateGroupFileCommand,
    RemovePathCommand,
    CreateIdsFileCommand,
    CreateGroupCommand,
    RemoveGroupCommand,
    MovePathCommand,
    MoveEllipticsDataCommand,
    LockBackendCommand,
    CreateFileMarkerCommand,
    UnlockBackendCommand,
    RemoveGroupFileCommand,
    CheckFileSystemCommand,
    PingCommand,
    CheckGroupLocation,
)


COMMAND_SUBPROCESS = {}

for subprocess_type in __all__:
    if not issubclass(subprocess_type, BaseCommand):
        # sanity check
        continue

    COMMAND_SUBPROCESS[subprocess_type.COMMAND] = subprocess_type


def subprocess_factory(cmd):
    if cmd[0] not in COMMAND_SUBPROCESS:
        raise ValueError('Unsupported command "{}"'.format(cmd[0]))

    return COMMAND_SUBPROCESS[cmd[0]]
