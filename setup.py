from setuptools import setup

setup(
    name="stage_from_temp",
    version="0.1.0",
    packages=['stage'],
    install_requires=[
        'Click',
        'DS3-SDK@git+https://github.com/spectralogic/ds3_python3_sdk@v5.0.3#egg=DS3-SDK'
    ],
    entry_points={
        'console_scripts': ['stage=stage.stage:main']
    })
