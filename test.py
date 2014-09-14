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

#volumes = conn.get_all_volumes()
snapshots = conn.get_all_snapshots(filters={'owner-id': owner_id})
#snapshots = conn.get_all_snapshots(["snap-2956bee8"])
#snapshots = conn.get_all_snapshots(filters={'volume-id': volume.id})

first_snapshot = snapshots[0] #  first item in list

# Debugging

print snapshots
#print first_snapshot.tags
#print volumes
print dir(first_snapshot)
#print dir(volumes)
#print first_snapshot.__dict__
#print volumes.__dict__
# print "press 'c' when you are done with debugging"
# import pdb ; pdb.set_trace()  # breakpoint once we've established our obj
