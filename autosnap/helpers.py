'''Autosnap - volume and snapshot lifecycle management tool'''

import boto.ec2
import datetime
import ConfigParser

# Date stuff
current_date = datetime.date.today().strftime("%j")
expiration_date = int(datetime.date.today().strftime("%j")) + 7

### Volume level

def manage_single_vol(volume):
    """Manage a volume in region"""
    return

def manage_all_vols(volumes):
    """Manage all volumes in region"""

    print 'Adding volumes to autosnap'
    vol_count = 0

    # Skip if tagged already
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

def unmanage_single_vol(volume):
    """Unmanage a volume in region"""
    return

def unmanage_all_vols(volumes):
    """Unmanage all volumes in region"""

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
def filter_vol_by_tag(volumes):
    """Filter volumes based on tags"""
    return

def vol_in_arrary(vol):
    """Check to see if vol is part of an array"""
    return

# When a snapshot gets created, add a 'date_created' tag
#first_snapshot.add_tag('date_created', "{0}".format(current_date))

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
#first_snapshot.add_tag('retention', '7')

# Run cleanup function to see if any snapshots are older than the expiration

