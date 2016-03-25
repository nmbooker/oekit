#!/usr/bin/env python

import unittest
import argparse
from oekit.config.argparse import add_login_args, ArgsConfig

class TestArgparseConf(unittest.TestCase):
    def setUp(self):
        parser = argparse.ArgumentParser()
        add_login_args(parser)
        self.url = 'http://example.org:8069'
        self.user = 'admin'
        self.password = 'password'
        self.dbname = 'foodb'
        options = parser.parse_args([
            '--url', self.url,
            '--user', self.user,
            '--password', self.password,
            '--dbname', self.dbname,
        ])
        self.conf = ArgsConfig(options)

    def test_argparse(self):
        self.assertEqual(self.conf['url'], self.url)
        self.assertEqual(self.conf['user'], self.user)
        self.assertEqual(self.conf['password'], self.password)
        self.assertEqual(self.conf['dbname'], self.dbname)
