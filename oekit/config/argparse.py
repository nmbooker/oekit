
"""oekit config source for using argumentparser to log in

Example:

    import argparse
    from oekit.config.argparse import add_login_args, ArgsConfig
    from oekit.clientfactory import peek
    parser = argparse.ArgumentParser()
    add_login_args(parser)
    options = parser.parse_args()
    oe = peek.ClientFactory().connect(AttrsConfig(options))

"""

from .attrs import AttrsConfig

def add_url_arg(parser):
    """Add URL argument to ArgumentParser.

    Useful for scripts that work with the database manager instead
    of logging into the databases themselves.
    """
    parser.add_argument('--url', help='URL of the Odoo server')

def add_login_args(parser):
    """Add arguments to an ArgumentParser.

    Your 'options' object will then have the attributes necessary
    to be passed into the connect() method of a client factory.
    """
    add_url_arg(parser)
    parser.add_argument('--dbname', help='database name to connect to')
    parser.add_argument('--user', help='name of user to log in as')
    parser.add_argument('--password', help='password to log in with')

class ArgsConfig(AttrsConfig):
    """Config adapter for argparse namespace object.
    """
    pass

__COPYRIGHT__ = """

This program is part of oekit: https://github.com/nmbooker/oekit

Copyright (c) 2015-2016 Nicholas Booker <NMBooker@gmail.com>

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 3
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""
