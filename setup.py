#! /usr/bin/env python

import setuptools

setuptools.setup(
    name = 'oekit',
    version = '0.15',
    packages = setuptools.find_packages(),
    install_requires = ['erppeek>=1.6'],
    scripts = [
        'oe_dump_csv',
        'oe_describe',
        'oe_list_models',
        'oe_selection',
        'odoo.createdb',
        'odoo.dropdb',
        'odoo.insmod',
        'odoo.rmmod',
        'odoo.create_records',
        'odoo.xmlid_of',
        'odoo.backupdb',
    ],
)
