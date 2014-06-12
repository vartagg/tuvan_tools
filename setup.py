#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')


setup(
    name='tuvan_tools',
    version='0.1.0',
    description='Yet another Python toolkit.',
    long_description=readme + '\n\n' + history,
    author='Vladimir Chub',
    author_email='vartagg@users.noreply.github.com',
    url='https://github.com/vartagg/tuvan_tools',
    packages=[
        'tuvan_tools',
    ],
    py_modules=['tuvan_tools'],
    include_package_data=True,
    license="BSD",
    zip_safe=False,
    keywords='tuvan_tools',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
    ],
)
