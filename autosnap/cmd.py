import logging
from pytool.cmd import Command
import ec2_connection
import boto.ec2
import helpers

class Main(Command):
    """autosnap command line tool"""

    def set_opts(self):
        """Command line options"""
        self.opt('--list-vols', action='store_true',
                help='list managed volumes')

        self.opt('--manage-vols', action='store_true',
                help='manage all volumes in region with autosnap')

        self.opt('--unmanage-vols', action='store_true',
                help='unmanage all vols')

        self.opt('--list-snaps',
                help='list managed snapshots')

        self.opt('--verbose', action='store_true',
                help='Increase verbosity')

        self.opt('--config',
                help='override config file (default is ../.config)')

        self.opt('--dry-run',
                help='list snapshots that will be taken, does not create them')

        self.opt('--version', action='version', version='0.0.1')

    def run(self):

        a = self.args
        c = ec2_connection.get_connection()
        volumes = c.get_all_volumes()

        # List managed volumes
        if a.list_vols == True:
            helpers.list_managed_vols(volumes)

        # Manage all volumes
        if a.manage_vols == True:
            helpers.manage_all_vols(volumes)

        # Unmanage all volumes
        if a.unmanage_vols == True:
           helpers.unmanage_all_vols(volumes)

