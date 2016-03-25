#!/usr/bin/env python

import argparse
from oekit.config.argparse import add_login_args, ArgsConfig

def test_argparse():
    parser = argparse.ArgumentParser()
    add_login_args(parser)
    url = 'http://example.org:8069'
    user = 'admin'
    password = 'password'
    dbname = 'foodb'
    options = parser.parse_args([
        '--url', url,
        '--user', user,
        '--password', password,
        '--dbname', dbname,
    ])
    conf = ArgsConfig(options)
    assert conf.get('url') == url
    assert conf.get('user') == user
    assert conf.get('password') == password
    assert conf.get('dbname') == dbname
