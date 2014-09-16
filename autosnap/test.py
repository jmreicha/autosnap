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
print tags
'''

def test_vols(volumes):
    """Manage all volumes in region"""

    print 'Adding volumes to autosnap'

    # Skip if tagged already
    for volume in volumes:
        for tag in tags:
            print volume.tags
            print tag.name.startswith('is_managed')
            print volume.__dict__
            print "press 'c' when you are done with debugging"
            import pdb ; pdb.set_trace()  # breakpoint
    return

def manage_all_vols(volumes):

    vol_count = 0

    for volume in volumes:
        if not volume.tags:
            volume.add_tag('is_managed', True)
            vol_count = vol_count + 1
            continue
        managed = False
        for tag in volume.tags:
            if tag == 'is_managed':
                managed = True
                break
        if not managed:
            volume.add_tag('is_managed', True)
    if vol_count > 0:
        if vol_count = 1:
            print str(vol_count) + ' volume added to autosnap'
        else:
            print str(vol_count) + ' volumes added to autosnap'

    return


manage_all_vols(volumes)

'''
# Date stuff
current_date = datetime.date.today().strftime("%j")
expiration_date = int(datetime.date.today().strftime("%j")) + 7
'''

