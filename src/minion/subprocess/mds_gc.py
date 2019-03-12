from minion.subprocess.base_shell import BaseSubprocess
from minion.artifacts.exec_state import ExecStateArtifactsMixin


class MdsGcSubprocess(ExecStateArtifactsMixin, BaseSubprocess):

    COMMAND = 'mds_gc'
