
"""oekit config - base stuff
"""

class BaseConfig(object):
    """Base config.

    Implement self._get(key), returning None if unset.
    """
    def __getitem__(self, key):
        val = self._get(key)
        if val is None:
            raise KeyError(key)
        return val

    def get(self, key, default=None):
        val = self._get(key)
        if val is None:
            return default
        return val

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
