from setuptools import setup

setup(
    # ...
    entry_points={
        'console_scripts':[
            'helloworld = hello:HelloWorld.console_script',
            ],
        },
    )

