
"""A simple kit for client-side OpenERP programming and testing.

Author: Nick Booker
License: GPLv3

Here are some of the modules:
    oeproxy: simplifies talking to an OpenERP server via XML-RPC a bit
    oe_client_env: get login info and an OEProxy using data from environment variables
    csvdump: helpers for dumping out records to CSV files
    oe_dateutil: helpers for validating, formatting and parsing dates for OpenERP
"""

from .. import oeproxy

class OEProxyClientFactory(object):
    """Client factory for oeproxy

    Example:

    factory = OEProxyClientFactory()
    config = OEClientChain(clients=[...])
    oe = factory.connect(config)
    """
    def connect(self, config):
        """Return a new OEProxy logged into the database configured in the
        environment.
        """
        oe = oeproxy.OEProxy(config['url'])
        oe.login(config['dbname'], config['user'], config['password'])
        return oe

__COPYRIGHT__ = """

This program is part of oekit: https://github.com/nmbooker/oekit

Copyright (c) 2017 Nicholas Booker <NMBooker@gmail.com>

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
