#!/usr/bin/env python

import os
from setuptools import setup

NAME = "kiwi"
DESCRIPTION = "Build On Demand AWS Hadoop Clusters"
LONG_DESCRIPTION = None
AUTHOR = "Sijo Franklin"
EMAIL = "franklinsijo@gmail.com"
URL = "https://github.com/franklinsijo/kiwi"
REQUIRES_PYTHON = ">=2.7.5"
LICENSE = "MIT"
VERSION = None

here = os.path.dirname(os.path.abspath(__file__))

if not VERSION:
    try:
        with open(os.path.join(here, 'VERSION'), 'r') as f:
            VERSION = f.read().strip('\n').strip()  
    except IOError:
        raise

if not LONG_DESCRIPTION:
    try:
        with open(os.path.join(here, 'README.md'), 'r') as f:
            LONG_DESCRIPTION = f.read()
    except IOError:
        LONG_DESCRIPTION = ""

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    license=LICENSE
)