#!/usr/bin/env python
import os

from setuptools import setup, find_packages

setup(
    name='autosnap',
    version='0.0.1',
    author='Joshua Reichardt',
    author_email='josh.reichardt@gmail.com',
    description='A command line tool for managing AWS volumes and snapshots',
    long_description=open('README.md').read(),
    url='https://github.com/jmreicha/autosnap',
    install_requires=['pytool', 'boto'],
    entry_points={
        'console_scripts':[
            'autosnap = autosnap.cmd:Main.console_script',
            ],
        },
    )

