#!/usr/bin/python

import boto.ec2
import datetime
import ConfigParser
from get_config import get_configuration

# Config
config_file = '../.config'
c = get_configuration(config_file)
print c.get('owner_id')

# Connection settings
conn = boto.ec2.connect_to_region(region,
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key)

print conn
print "press 'c' when you are done with debugging"
import pdb ; pdb.set_trace()  # breakpoint

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
        if vol_count == 1:
            print str(vol_count) + ' volume added to autosnap'
        else:
            print str(vol_count) + ' volumes added to autosnap'

    return

def unmanage_all_vols(volumes):
    """Manage all volumes in region"""

    print 'Removing volumes from autosnap'
    vol_count = 0

    # Only remove tagged vols
    for volume in volumes:
        if volume.tags:
            volume.remove_tag('is_managed', True)
            vol_count = vol_count + 1
            continue
        managed = True
        for tag in volume.tags:
            if tag == 'is_managed':
                managed = False
                break
        if managed:
            volume.remove_tag('is_managed', True)
    if vol_count > 0:
        if vol_count == 1:
            print str(vol_count) + ' volume removed from autosnap'
        else:
            print str(vol_count) + ' volumes removed from autosnap'

    return

def list_managed_vols(volumes):
    """Enumerate managed volumes in region"""

    managed_count = 0

    for volume in volumes:
        for tag in volume.tags:
            if tag == 'is_managed':
                managed = True
                managed_count = managed_count + 1
            if managed:
                print 'Volume ID: ' + str(volume.id) + 'Volume tags: ' + str(volume.tags)

    print str(managed_count) + ' total volumes managed'

    return

#manage_all_vols(volumes)
#list_managed_vols(volumes)
#unmanage_all_vols(volumes)

'''
# Date stuff
current_date = datetime.date.today().strftime("%j")
expiration_date = int(datetime.date.today().strftime("%j")) + 7
'''

