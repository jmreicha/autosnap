'''Read config and connect to AWS'''

import logging
import sys
import boto.ec2
from get_config import get_configuration

logger = logging.getLogger(__name__)

#c = get_config.get_configuration(config_file)
#print c

def get_connection():
    """ Connect to AWS """

    config_file = '../.config'
    c = get_config.get_configuration(config_file)

    #logger.info('Connecting to AWS EC2 in {}'.format(config.get('region'))

    # Connect using supplied credentials
    conn = boto.ec2.connect_to_region(config.get('region'),
        aws_access_key_id=config.get('aws_access_key_id'),
        aws_secret_access_key='aws_secret_access_key')

    if not conn:
        logger.error('An error occurred when connecting to EC2')
        sys.exit(1)

    return connection

c = get_connection()
print c


