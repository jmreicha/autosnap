#!/usr/bin/python

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

snapshots = conn.get_all_snapshots(filters={'owner-id': owner_id})
volumes = conn.get_all_volumes()
tags = conn.get_all_tags()

'''
volume = volumes[0]
print vol_tags
print volume.tags
print "dir\n"
print dir(volumes)
print "dict\n"
print volumes.__dict__
'''

def unmanage_all_vols(volumes):
    """Unmanage all volumes in region"""

    print 'Removing volumes from autosnap'

    # Don't add tag to volumes that have it already
    for volume in volumes:
        for tag in tags:
            if tag.name.startswith('is_managed'):
                volume.remove_tag('is_managed')
    return

unmanage_all_vols(volumes)

'''
# Date stuff
current_date = datetime.date.today().strftime("%j")
expiration_date = int(datetime.date.today().strftime("%j")) + 7

first_snapshot = snapshots[0] #  first item in list
first_volume = volumes[0] #  first item in list
#first_volume.add_tag('is_managed', True)

# Debugging

#print volumes
#print first_volume
#print first_volume.tags
#print volumes
#print dir(first_snapshot)
#print dir(volumes)
#print first_snapshot.__dict__
#print volumes.__dict__
# print "press 'c' when you are done with debugging"
# import pdb ; pdb.set_trace()  # breakpoint once we've established our obj
'''
