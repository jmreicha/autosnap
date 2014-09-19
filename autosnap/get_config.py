""" Configuration file parser """

import logging
import sys
from ConfigParser import SafeConfigParser, NoOptionError

logger = logging.getLogger(__name__)

def get_configuration(filename):
    """ Read config file"""

    logger.debug('Reading configuration from {}'.format(filename))
    conf = SafeConfigParser()
    conf.read(filename)

    if not conf:
        logger.error('Configuration file {} not found'.format(filename))
        sys.exit(1)

    if not conf.has_section('default'):
        logger.error('Missing [default] section in the configuration file')
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
        logger.error('Error in config file: {}'.format(err))
        sys.exit(1)

    return config

