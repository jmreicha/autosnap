import logging
from pytool.cmd import Command
import ec2_connection
import boto.ec2
import helpers
import get_config

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

        self.opt('--list-snaps', action='store_true',
                help='list managed snapshots')

        self.opt('--create-snaps', action='store_true',
                help='create a snapshot if it is managed')

        self.opt('--config',
                help='override config file (default is ../.config)')

        self.opt('--dry-run', action='store_true',
                help='list snapshots that will be taken, does not create them')

        self.opt('--verbose', action='store_true',
                help='Increase verbosity')

        self.opt('--version', action='version', version='0.0.1')

    def run(self):

        a = self.args
        c = ec2_connection.get_connection()
        conf = get_config.get_configuration('../.config')
        owner_id = conf.get('owner_id')

        volumes = c.get_all_volumes()
        snapshots = c.get_all_snapshots(filters={'owner-id': owner_id})

        # List managed volumes
        if a.list_vols == True:
             helpers.list_managed_vols(volumes)

        # Manage all volumes
        if a.manage_vols == True:
             helpers.manage_all_vols(volumes)

        # Unmanage all volumes
        if a.unmanage_vols == True:
            helpers.unmanage_all_vols(volumes)

        # Create snapshots
        if a.create_snaps == True:
            helpers.auto_create_snapshot(volumes)

