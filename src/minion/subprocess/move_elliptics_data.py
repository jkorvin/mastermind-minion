import glob
import os
import shutil

from tornado import gen

from minion.logger import cmd_logger
from minion.subprocess.base import BaseCommand


class MoveEllipticsDataCommand(BaseCommand):

    COMMAND = 'move_elliptics_data'
    REQUIRED_PARAMS = ('move_src', 'move_dst')

    @gen.coroutine
    def execute(self):
        try:
            assert os.path.dirname(self.params['move_src']) != self.params['move_dst']

            remove_index_files = []
            moved_files = []

            # Move data first, then indexes
            src_files = sorted(glob.glob(self.params['move_src']))
            for src_file in src_files:

                dst_file = os.path.join(self.params['move_dst'], os.path.basename(src_file))
                os.rename(src_file, dst_file)

                moved_files.append(src_file)

                if '.index' in src_file:
                    # src_file /srv/storage/38/2/kdb/data-0.1.index
                    # data_file = data-0.1
                    data_file = os.path.basename(src_file.split('.index')[0])
                    index_file = os.path.basename(src_file)
                    # Don't remove files that have been moved
                    data_index_files = [f for f in glob.glob(os.path.join(self.params['move_dst'], data_file) + '.index*') if os.path.basename(f) != index_file]
                    for data_index_file in data_index_files:
                        os.remove(data_index_file)
                        remove_index_files.append(data_index_file)
        except Exception:
            cmd_logger.exception(
                'Failed to execute move path by mask command: {} to {}'.format(
                    self.params['move_src'],
                    self.params['move_dst'],
                ),
                extra=self.log_extra,
            )
            raise

        cmd_logger.info(
            'Successfully performed move my mask task ({} to {}). Moved files: {}. Removed files: {}'.format(
                self.params['move_src'],
                self.params['move_dst'],
                moved_files,
                remove_index_files
            ),
            extra=self.log_extra,
        )
