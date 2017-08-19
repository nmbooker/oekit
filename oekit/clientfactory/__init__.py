
"""A simple kit for client-side OpenERP programming and testing.

Author: Nick Booker
License: GPLv3
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


class peek:
    """Client factories for erppeek.

    Example:

        factory = erppeek_factory.ClientFactory()
        config = OEClientChain(clients=[...])
        oe = factory.connect(config)
    """
    class Base(object):
        def __init__(self, verbose=False):
            self.verbose = verbose

    class DatabaseManagerFactory(Base):
        """Client factory for an erppeek.Client, but with just enough to do
        database management.
        """
        def connect(self, config):
            import erppeek
            return erppeek.Client(
                server=config['url'],
                verbose=self.verbose,
            )

    class ClientFactory(Base):
        """Client factory for erppeek, connected to a database.
        """
        def connect(self, config):
            """Return a new erppeek.Client.

            Note you must have the erppeek package in the python path
            for this to work, or you will get an ImportError on call.
            """
            import erppeek
            return erppeek.Client(
                server=config['url'],
                db=config['dbname'],
                user=config['user'],
                password=config['password'],
                verbose=self.verbose
            )

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
