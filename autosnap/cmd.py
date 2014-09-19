import logging
from pytool.cmd import Command

class Main(Command):
    """autosnap command line tool"""

    def set_opts(self):
        """Command line options"""
        self.opt('--volume',
                help='list managed volumes')

        self.opt('--snapshot',
                help='list managed snapshots')

        self.opt('--verbose',
                help='turn up verbosity level')

        self.opt('--config',
                help='override config file (default is ../.config)')

        self.opt('--region',
                help='override region (defaults to config file region)')

        self.opt('--dry-run',
                help='list snapshots that will be taken, does not create them')

        self.opt('--version', action='version', version='0.0.1')

    def run(self):
        print "Hello world"

