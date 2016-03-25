#!/usr/bin/env python

import os
from oekit.config.env import EnvConfig

def test_env():
    os.environ['TEST_URL'] = 'http://example.com:8069'
    os.environ['TEST_USER'] = 'admin'
    os.environ['TEST_PASSWORD'] = 'password'
    os.environ['TEST_DBNAME'] = 'foodb'
    env = EnvConfig('TEST_')
    assert env.url == 'http://example.com:8069'
    assert env.user == 'admin'
    assert env.password == 'password'
    assert env.dbname == 'foodb'
