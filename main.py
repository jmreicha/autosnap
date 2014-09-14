
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

snapshots = conn.get_all_snapshots(['snap-2956bee8']) #  returns a list()
#snapshots = conn.get_all_snapshots(filters={'volume-id': volume.id})

first_snapshot = snapshots[0] #  first item in list

# Debugging
print first_snapshot.tags
print dir(first_snapshot)
print first_snapshot.__dict__
# print "press 'c' when you are done with debugging"
# import pdb ; pdb.set_trace()  # breakpoint once we've established our obj

### Volume level

def manage_volume():
    """Manage a volume in region"""

def manage_all_volumes():
    """Manage all volumes in region"""

def unmanage_volume():
    """Unmanage a volume in region"""

def unmanage_all_volumes():
    """Unmanage all volumes in region"""

def list_managed_volumes():
    """Enumerate managed volumes in region"""

    count = 0

# Managed by our tool?
first_snapshot.add_tag('is_managed', True)

# When a snapshot gets created, add a 'date_created' tag
first_snapshot.add_tag('date_created', "{0}".format(current_date))

# Is volume part of an array?

### Snapshot level

def create_snapshot(volume):
    """Manually create a snapshot"""

def delete_snapshot(volume):
    """Manually remove a snapshot"""

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

