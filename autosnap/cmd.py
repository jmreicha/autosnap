import logging
from pytool.cmd import Command

class Main(Command):
    """autosnap command line tool"""

    def set_opts(self):
        """Command line options"""
        self.opt('--volume', '-v', help='list managed volumes')
        self.opt('--snapshot', '-s', help='list snapshots')
        self.opt('--log-level', '-l', help='set logging level')
        self.opt('--config', '-c',
                help='override config file (default is ../.config)')
        self.opt('--region', '-r',
                help='override region (defaults to config file region)')
        self.opt('--dry-run', '-d',
                help='list snapshots that will be taken, does not create them')
        self.opt('--version' action='version', version=autosnap.__version__)

    def run(self):
        #server.run_server(port=self.args.port, host=self.args.host)
