from pytool.cmd import Command
import helpers
import os

class Main(Command):
    """autosnap command line tool"""

    def set_opts(self):
        """Command line options"""
        self.opt('--list-vols', action='store_true',
                help='list managed volumes')

        self.opt('--manage-vols', action='store_true',
                help='manage all volumes')

        self.opt('--unmanage-vols', action='store_true',
                help='unmanage all volumes')

        self.opt('--list-snaps', action='store_true',
                help='list managed snapshots')

        self.opt('--create-snaps', action='store_true',
                help='create a snapshot if it is managed')

        self.opt('--remove-snaps', action='store_true',
                help='create a snapshot if it is managed')

        self.opt('--dry-run', action='store_true',
                help='list snapshots that will be taken, does not create them')

        self.opt('--verbose', action='store_true',
                help='Increase verbosity')

        self.opt('--version', action='version', version='0.0.1')

    def run(self):

        a = self.args
        volumes = helpers.list_vols()

        # Default behavior
        helpers.get_stats()

        ### TODO Create config if missing
        if not os.path.isfile('../.config'):
            print 'no config file found.  Would you like to create one?'

        # get region
        # get aws_access_key
        # get aws_secret_key
        # create/open ../.config and update or create these vars

        # List managed volumes
        if a.list_vols == True:
             helpers.list_managed_vols(volumes)

        # Manage all volumes
        if a.manage_vols == True:
             helpers.manage_all_vols(volumes)

        # Unmanage all volumes
        if a.unmanage_vols == True:
            helpers.unmanage_all_vols(volumes)

        # Create snapshots for managed volumes
        if a.create_snaps == True:
            helpers.auto_create_snapshot(volumes)

        # List all snapshots
        if a.list_snaps == True:
            helpers.list_snapshots()

