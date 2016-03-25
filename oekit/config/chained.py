
"""OpenERP client using a chain of fallbacks.
"""

from .base import BaseConfig

class OEConfigChain(BaseConfig):
    """Get client login info.
    
    This implementation checks a series of configs in order,
    and the first config to return a value other than None
    from its get() method wins.
    """
    def __init__(self, configs):
        self.configs = configs

    def _get(self, key):
        for config in self.configs:
            value = config.get(key, None)
            if value is not None:
                return value
        return None

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
