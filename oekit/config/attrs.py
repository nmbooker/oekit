
"""Ada

Example:

    from oekit.config.attrs import AttrsConfig
    from oekit.clientfactory import peek
    obj = object()
    obj.url = 'http://foo.example.org:8069'
    oe = peek.DatabaseManagerFactory().connect(AttrsConfig(obj))

"""

class AttrsConfig(object):
    """Adapt an object that may have one or more of 'url', 'dbname',
    'password' and 'user' attributes properties.

    Essentially converts AttributeError on these attrs to a return None,
    and hides all other methods on the object to avoid accidental damage.
    """
    def __init__(self, obj):
        self._obj = obj

    @property
    def url(self):
        return self._getopt('url')

    @property
    def dbname(self):
        return self._getopt('dbname')

    @property
    def password(self):
        return self._getopt('password')

    @property
    def user(self):
        return self._getopt('user')

    def _getopt(self, name):
        if hasattr(self._obj, name):
            return getattr(self._obj, name)
        return None

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
