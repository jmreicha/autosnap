import logging
from pytool.cmd import Command

class Main(Command):
    """autosnap command line tool"""

    def set_opts(self):
        """Command line options"""
        self.opt('--version', action='version', version=autosnap.__version__)

    def run(self):
        server.run_server(port=self.args.port, host=self.args.host)
