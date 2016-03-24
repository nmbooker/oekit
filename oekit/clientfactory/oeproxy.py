
"""Client factory for oeproxy.

Example:

    factory = OEProxyClientFactory()
    config = OEClientChain(clients=[...])
    oe = factory.connect(config)
"""

import ..oeproxy

class OEProxyClientFactory(object):
    """Client factory for oeproxy
    """
    def connect(self, config):
        """Return a new OEProxy logged into the database configured in the
        environment.
        """
        oe = oeproxy.OEProxy(config.url)
        oe.login(config.dbname, config.user, config.password)
        return oe

__COPYRIGHT__ = """

This program is part of oekit: https://github.com/nmbooker/oekit

Copyright (c) 2016 Nicholas Booker <NMBooker@gmail.com>

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
