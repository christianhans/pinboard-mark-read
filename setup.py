#!/usr/bin/env python

from setuptools import setup

setup(
    name='Pinboard Mark as Read',
    version='1.0',
    packages=['pinboard_mark_read'],
    install_requires=[
        'Flask>=1.1.1',
        'Flask-Limiter>=1.1.0',
        'gunicorn>=20.0.4',
        'pinboard>=2.1.8'
    ]
)