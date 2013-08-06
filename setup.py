#! /usr/bin/env python

import setuptools

setuptools.setup(
    name = 'oekit',
    version = '0.3',
    packages = setuptools.find_packages(),
    scripts = ['oe_dump_csv', 'oe_describe'],
)
