#!/usr/bin/env python

"""Test chaining of configs.
"""

from oekit.config.chained import OEConfigChain

conf_global = {
    'url': 'http://localhost:8069',
    'dbname': 'odoo',
}

conf_local = {
    'dbname': 'test',
    'user': 'admin',
    'password': 'topsecret',
}

chain = OEConfigChain(configs=[conf_local, conf_global])

def test_fall_through_global():
    assert chain.get('url') == 'http://localhost:8069'


def test_local_only():
    assert chain.get('user') == 'admin'
    assert chain.get('password') == 'topsecret'


def test_local_trumps_global():
    assert chain.get('dbname') == 'test'


def test_no_match():
    assert chain.get('foo') is None
