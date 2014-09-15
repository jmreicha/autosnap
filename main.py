
import boto.ec2
import datetime
import ConfigParser

# Config
config_file = '.config'
config = ConfigParser.ConfigParser()
config.read(config_file)

region = config.get('default', 'region')
aws_access_key_id = config.get('default', 'aws_access_key_id')
aws_secret_access_key = config.get('default', 'aws_secret_access_key')
owner_id = config.get('default', 'owner_id')

# Connection settings
print 'Connecting to AWS'
conn = boto.ec2.connect_to_region(region,
	aws_access_key_id=aws_access_key_id,
	aws_secret_access_key=aws_secret_access_key)

# Date stuff
current_date = datetime.date.today().strftime("%j")
expiration_date = int(datetime.date.today().strftime("%j")) + 7

volumes = conn.get_all_volumes()
snapshots = conn.get_all_snapshots(filters={'volume-id': volume.id})

# Debugging
# print "press 'c' when you are done with debugging"
# import pdb ; pdb.set_trace()  # breakpoint once we've established our obj

### Volume level

def manage_single_vol(volume):
    """Manage a volume in region"""
    return

def manage_all_vols(volumes):
    """Manage all volumes in region"""

    print 'Adding volumes to autosnap'

    # Skip if tagged already
    for volume in volumes:
        for tag in tags:
            if tag.name.startswith('is_managed'):
                pass
            else:
                volume.add_tag('is_managed', True)
    return

def unmanage_single_vol(volume):
    """Unmanage a volume in region"""
    return

def unmanage_all_vols(volumes):
    """Unmanage all volumes in region"""

    print 'Removing volumes from autosnap'

    # Only remove tagged vols
    for volume in volumes:
        for tag in tags:
            if tag.name.startswith('is_managed'):
                volume.remove_tag('is_managed')
    return

def list_managed_vols(volumes):
    """Enumerate managed volumes in region"""

    count = 0

    for volume in volumes:
        if volume.get_key_pair('is_managed') == True:
            print volume, volume.id, volume.tags
            count += count + 1

    print count + " total volumes managed"
    return

def filter_vol_by_tag(volumes):
    """Filter volumes based on tags"""
    return

# When a snapshot gets created, add a 'date_created' tag
first_snapshot.add_tag('date_created', "{0}".format(current_date))

# Is volume part of an array?

### Snapshot level

def create_snapshot(volume):
    """Manually create a snapshot for a vol"""

def delete_snapshot(volume):
    """Manually remove a snapshot for a vol"""

def auto_create_snapshot(volume):
    """Automatically create a snpashot if it is managed by our tool"""

def auto_delete_snapshot(volume):
    """Automatically expire a snapshot if it is older than its retention tag"""

def list_managed_snapshots(snapshot):
    """Enumerate managed snapshots in region"""

    counter = 0

def create_ami():
    """Create an AMI from a snapshot"""

# When a snapshot gets created, add a 'retention' tag
first_snapshot.add_tag('retention', '7')

# Run cleanup function to see if any snapshots are older than the expiration

