Stage from Pool
===============

This command line utility is designed to automate staging content
to cache that is written to a temporary pool.  The intention is to aid
with migrating between pools with temporary persistence rules.

Installation
============

This command line tool requires Python 3 and can be installed with pip.
To install run: `pip3 install -e git+https://github.com/SpectraLogic/stage_from_pool#egg=stage`

Usage
===

First make sure that the `DS3_ENDPOINT`, `DS3_ACCESS_KEY`, and
`DS3_SECRET_KEY` are all set.  These are the same settings as used by
the [ds3_java_cli](https://github.com/SpectraLogic/ds3_java_cli#linux-configuration)

Once the environment variables are set then run `stage POOL_NAME
BUCKET_NAME` where `POOL_NAME` is the name of the pool you which to stage content from
and `BUCKET_NAME` is the bucket that you which to stage the content in.

Only the content that's in `BUCKET_NAME` will be staged from the Pool.  All other content will be left alone.
