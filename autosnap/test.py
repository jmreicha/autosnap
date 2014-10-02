#!/usr/bin/python

import helpers
import datetime
from datetime import timedelta

snaps = helpers.get_snapshots()

for snap in snaps:

        current_date = datetime.datetime.now()
        snap_date = snap.start_time
        if snap.tags.get('retention(days)') is None:
            retention = 0
        else:
            retention = snap.tags.get('retention(days)')

        expiration = current_date - timedelta(days=int(retention))

        print 'ID: ' + snap.id
        print 'Current date: ' + str(current_date)
        print 'Snapshot create: ' + str(snap_date)
        print 'Retention: ' + str(retention)
        print 'Expiration date: ' + str(expiration)
