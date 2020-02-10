from setuptools import setup, find_packages

setup(
    name="spectra_support",
    version="0.2.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'DS3-SDK@git+https://github.com/spectralogic/ds3_python3_sdk@v5.0.3#egg=DS3-SDK'
    ],
    entry_points={
        'console_scripts': ['spectra-support=stage.stage:support']
    })
