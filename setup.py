#!/usr/bin/env python

from setuptools import setup

setup(
    name='Pinboard Mark as Read',
    version='1.0.1',
    packages=['pinboard_mark_read'],
    install_requires=[
        'Flask>=2.0.1',
        'Flask-Limiter>=1.4.0',
        'gunicorn>=20.1.0',
        'pinboard>=2.1.8'
    ]
)
