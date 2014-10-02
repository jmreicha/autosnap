from pytool.cmd import Command
import helpers
import get_config
import os

class Main(Command):
    """autosnap command line tool"""

    def set_opts(self):
        """Command line options"""

        self.opt('--config', action='store_true',
                help='create or modify configuration file')

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

        # Create config if missing
        if not os.path.isfile('../.config'):
            print 'no config file found\n'
            default_region = raw_input('Default region name: ')
            aws_key_id = raw_input('AWS Access Key ID: ')
            aws_access_key = raw_input('AWS Secret Access Key: ')
            owner_id = raw_input('Owner ID: ')

            get_config.set_configuration(default_region, aws_key_id, aws_access_key, owner_id)
            return

        # Update config
        if a.config == True:
            aws_key_id = raw_input('AWS Access Key ID: ')
            aws_access_key = raw_input('AWS Secret Access Key: ')
            default_region = raw_input('Default region name: ')
            owner_id = raw_input('Owner ID: ')

            get_config.set_configuration(default_region, aws_key_id, aws_access_key, owner_id)
            return

        volumes = helpers.list_vols()

        # List managed volumes
        if a.list_vols == True:
             helpers.list_managed_vols(volumes)
             return

        # Manage all volumes
        if a.manage_vols == True:
             helpers.manage_all_vols(volumes)
             return

        # Unmanage all volumes
        if a.unmanage_vols == True:
            helpers.unmanage_all_vols(volumes)
            return

        # Create snapshots for managed volumes
        if a.create_snaps == True:
            helpers.auto_create_snapshot(volumes)
            return

        # List all snapshots
        if a.list_snaps == True:
            helpers.print_snapshots()
            return

        # Remove managed snapshots
        if a.remove_snaps == True:
            helpers.delete_snapshots()
            return

        # TODO only print if config not changed
        # Print stats if nothing gets called
        helpers.get_stats()

