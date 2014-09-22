'''Read config and connect to AWS'''

import logging
import sys
import boto.ec2
import get_config

logger = logging.getLogger(__name__)

def get_connection():
    """ Connect to AWS """

    # Read config
    config = '../.config'
    config = get_config.get_configuration(config)
    #logger.info('Connecting to AWS EC2 in {}'.format(config.get('region'))

    # Connect using supplied credentials
    conn = boto.ec2.connect_to_region(config.get('region'),
        aws_access_key_id=config.get('aws_access_key_id'),
        aws_secret_access_key=config.get('aws_secret_access_key'))

    if not conn:
        logger.error('An error occurred when connecting to EC2')
        sys.exit(1)

    return conn

