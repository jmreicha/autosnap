""" Configuration file parser """

import logging
import sys
from ConfigParser import SafeConfigParser, NoOptionError, ConfigParser

def get_configuration(filename):
    """Read config file"""

    conf = SafeConfigParser()
    conf.read(filename)

    if not conf:
        print 'Configuration file {} not found'.format(filename)
        sys.exit(1)

    if not conf.has_section('aws_default'):
        print 'Missing [aws_default] section in the configuration file'
        sys.exit(1)

    try:

        region = conf.get('aws_default', 'region')
        aws_access_key_id = conf.get('aws_default', 'aws_access_key_id')
        aws_secret_access_key = conf.get('aws_default', 'aws_secret_access_key')
        owner_id = conf.get('aws_default', 'owner_id')

        config = {
            'region': region,
            'aws_access_key_id': aws_access_key_id,
            'aws_secret_access_key': aws_secret_access_key,
            'owner_id': owner_id
        }

    except NoOptionError as err:
        print 'Error in config file: {}'.format(err)
        sys.exit(1)

    return config

def set_configuration(aws_region, aws_access_key_id, aws_secret_access_key, owner_id):
    """Write config file"""

    conf = ConfigParser()

    # Populate config
    conf.add_section('aws_default')
    conf.set('aws_default', 'region', str(aws_region))
    conf.set('aws_default', 'aws_access_key_id', str(aws_access_key_id))
    conf.set('aws_default', 'aws_secret_access_key', str(aws_secret_access_key))
    # Skip owner_id if blank
    if owner_id == '':
        pass
    else:
        conf.set('aws_default', 'owner_id', str(owner_id))

    # Write config to file
    with open('../.config', 'wb') as configfile:
        conf.write(configfile)

    return conf

