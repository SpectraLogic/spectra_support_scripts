Support Scripts
===============

This command line utility is designed to automate various support
functions. The intention is to aid support by having common tools
that can be used at various customer sites. 

Installation
============

This command line tool requires Python 3 and can be installed with pip.
To install run: `pip3 install -e git+https://github.com/SpectraLogic/spectra_support_scripts#egg=spectra-support`

Usage
===

First make sure that the `DS3_ENDPOINT`, `DS3_ACCESS_KEY`, and
`DS3_SECRET_KEY` are all set.  These are the same settings as used by
the [ds3_java_cli](https://github.com/SpectraLogic/ds3_java_cli#linux-configuration)

Once the environment variables are set then run `spectra-support` to see
the list of supported commands.

Commands
=======

###clear-suspect-blobs
The `clear-suspect-blobs` command takes no arguments and will clear all
suspect tape blobs.

###list-suspect-blobs
The `list-suspect-blobs` command takes no arguments and will list all
suspect tape blobs.

###stage
The `stage` command is used to stage content from an existing BP pool.
This command takes 2 arguments `BUCKET_NAME` and `POOL_NAME`.
`BUCKET_NAME` is the name of the bucket that you wish to stage content
in, and `POOL_NAME` is the name of the pool you wish to stage content
from.  If the bucket is not on the pool then no stage jobs will be
submitted.

Help
====

There is a general help menu which you can invoke with `spectra-support
--help`.  This will list all the available commands and any common options.  For each command
you can also type `spectra-support stage --help` and that will list any
arguments or options unique to that command.
