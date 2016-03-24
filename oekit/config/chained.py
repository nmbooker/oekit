
"""OpenERP client using a chain of fallbacks.
"""

from .base import OEClientConfigError

class OEClientChain(object):
    """Get client login info.
    """
    def __init__(self, clients):
        self.clients = clients

    def _get_first_attr(self, attrname):
        for client in clients:
            try:
                value = getattr(client, attrname)
            except OEClientConfigError:
                value = None
            if value is not None:
                return value
            raise OEClientConfigError('url')

    @property
    def url(self):
        """The URL"""
        return self._get_first_attr('url')

    @property
    def dbname(self):
        """The database name
        """
        return self._get_first_attr('dbname')

    @property
    def user(self):
        """The username
        """
        return self._get_first_attr('user')

    @property
    def password(self):
        """The password
        """
        return self._get_first_attr('password')


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
