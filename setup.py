from setuptools import setup, find_packages

__version__ = '0.0.1'

setup(
    name='autosnap',
    version=__version__,
    author='Joshua Reichardt',
    author_email='josh.reichardt@gmail.com',
    description='A command line tool for managing AWS volumes and snapshots',
    url='https://github.com/jmreicha/autosnap',
    install_requires=['pytool', 'boto'],
    entry_points={
        'console_scripts':[
            'autosnap = autosnap.cmd:Main.console_script',
            ],
        },
    )

