
"""oekit config source using environment variables for logging in.

This allows you to write quick and dirty test scripts.

I wouldn't consider it secure for writing production scripts because
it involves saving your password in an environment variable.
For production, you might want to take info at the command line and
prompt for a password (without echoing) instead.
"""

import os
from .base import BaseConfig

class EnvConfig(BaseConfig):
    """Get client login info from the environment.

    By default, the information will be retrieved from the environment
    variables:
     * OE_CLIENT_URL
     * OE_CLIENT_DBNAME
     * OE_CLIENT_USER
     * OE_CLIENT_PASSWORD

    You can specify an alternative prefix to OE_CLIENT_ by passing it
    into the constructor.
    """
    def __init__(self, prefix="OE_CLIENT_"):
        """
        prefix: The prefix to prepend to the environment variable names.
                Default: OE_CLIENT_
        """
        self.prefix = prefix

    def _get(self, key):
        return self._environ(key.upper())

    def _environ(self, suffix):
        """Return value of environment variable with given suffix."""
        return os.getenv(self._var(suffix))

    def _var(self, suffix):
        """Return the full environment variable name."""
        return self.prefix + suffix

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
