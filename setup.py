#!/usr/bin/python
# -*- coding: utf8 -*-

import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-shibboleth-eds',
    version='0.7',
    packages=find_packages(),
    include_package_data=True,
    license='Apache 2.0',
    description='Django app to embed Shibboleth Embedded Discovery Service into your Django project.',
    long_description=README,
    url='https://github.com/hu-berlin-cms/django-shibboleth-eds',
    author='Enno Gröper',
    author_email='enno.groeper@cms.hu-berlin.de',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
