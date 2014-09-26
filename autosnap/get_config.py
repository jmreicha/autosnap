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

    if not conf.has_section('default'):
        print 'Missing [default] section in the configuration file'
        sys.exit(1)

    try:

        region = conf.get('default', 'region')
        aws_access_key_id = conf.get('default', 'aws_access_key_id')
        aws_secret_access_key = conf.get('default', 'aws_secret_access_key')
        owner_id = conf.get('default', 'owner_id')

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
    conf.add_section('default')
    conf.set('default', 'region', str(aws_region))
    conf.set('default', 'aws_access_key_id', str(aws_access_key_id))
    conf.set('default', 'aws_secret_access_key', str(aws_secret_access_key))
    conf.set('default', 'owner_id', str(owner_id))

    # Write config to file
    with open('../.config', 'wb') as configfile:
        conf.write(configfile)

    return conf

