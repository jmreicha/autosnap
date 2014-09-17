import logging
from pytool.cmd import Command

class Main(Command):
    """
    autosnap command line tool

    See autosnap --help for help info.

    Example usage::

        autosnap -v

    """

    def set_opts(self):
        """Command line options"""
        self.opt('--volume', '-v',
                help='list managed volumes')

        self.opt('--snapshot', '-s',
                help='list snapshots')

        self.opt('--log-level', '-l',
                help='set logging level')

        self.opt('--config', '-c',
                help='override config file (default is ../.config)')

        self.opt('--region', '-r',
                help='override region (defaults to config file region)')

        self.opt('--dry-run', '-d',
                help='list snapshots that will be taken, does not create them')

        self.opt('--version', action='version', version='0.0.1')

    def run(self):
        print "Hello world"

