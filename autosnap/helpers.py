'''Autosnap - volume and snapshot lifecycle management tool'''

import datetime
from datetime import timedelta
from dateutil.parser import parse as parse_date
import get_config
import ec2_connection

### Get statistics

def get_stats():
    """Helper for listing autosnap stats"""

    conf = get_config.get_configuration('../.config')
    conn = ec2_connection.get_connection()

    # Volumes
    volumes = conn.get_all_volumes()

    vol_count = 0

    for volume in volumes:
        vol_count = vol_count + 1

    # Snapshots
    owner_id = conf.get('owner_id')
    snapshots = conn.get_all_snapshots(filters={'owner-id': owner_id})

    snap_count = 0

    for snap in snapshots:
        snap_count = snap_count + 1

    # Region
    region = conf.get('region')

    print 'Autosnap stats\n'
    print 'Current region:    ' + '%15s' % (region)
    print 'Volumes managed:   ' + '%15s' % str(vol_count)
    print 'Snapshots managed: ' + '%15s' % str(snap_count)

### Volume level

def list_vols():
    """Helper to return volumes"""

    conn = ec2_connection.get_connection()
    volumes = conn.get_all_volumes()

    return volumes

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
                print 'Volume ID: ' + str(volume.id) + ' Volume size: ' + str(volume.size) + 'GB ' + ' Volume tags: '+ str(volume.tags)

    print str(managed_count) + ' total volumes managed'

    return

### Snapshot level

def auto_create_snapshot(volumes):
    """Automatically create a snpashot if it is managed"""

    print "Creating snapshots"
    date = datetime.datetime.now()

    for volume in volumes:
        for tag in volume.tags:
            if tag == 'is_managed':
                managed = True
            if managed:
                desc = str(volume.id + '(' + date.strftime('%m-%d-%y') + ')')
                # TODO check if snapshot for today's date already exists
                snap = volume.create_snapshot(desc)
                snap.add_tag('Name', '{0}'.format(desc))
                snap.add_tag('date_created', '{0}'.format(date.strftime('%m-%d-%y')))
                snap.add_tag('retention(days)', '7')

    return

def print_snapshots():
    """Print all snapshots"""

    # List only owner snapshots
    conf = get_config.get_configuration('../.config')
    owner_id = conf.get('owner_id')

    conn = ec2_connection.get_connection()
    snapshots = conn.get_all_snapshots(filters={'owner-id': owner_id})

    for snap in snapshots:
        print snap.tags

    return

def get_snapshots():
    """List all snapshots"""

    # List only owner snapshots
    conf = get_config.get_configuration('../.config')
    owner_id = conf.get('owner_id')

    conn = ec2_connection.get_connection()
    snapshots = conn.get_all_snapshots(filters={'owner-id': owner_id})

    return snapshots

def delete_snapshots():
    """Expire snapshots"""

    # Current date
    current_date = datetime.datetime.now()
    #current_date = date.replace(tzinfo=None)

    # Get snapshots
    snapshots = get_snapshots()

    for snap in snapshots:

        snap_date = parse_date(snap.start_time)
        snap_date = snap_date.replace(tzinfo=None)

        if snap.tags.get('retention(days)') is None:
            retention = 0
        else:
            retention = snap.tags.get('retention(days)')
            expiration = current_date - timedelta(days=int(retention))

            if retention == 0:
                pass
            elif snap_date < expiration:
                print 'Deleting snapshot {}'.format(snap.id)
                snap.delete()

    return

def create_ami(snap_id):
    """Create an AMI from a snapshot"""

