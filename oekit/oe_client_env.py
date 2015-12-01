
"""OpenERP client using environment variables for logging in.

This allows you to write quick and dirty test scripts.

I wouldn't consider it secure for writing production scripts because
it involves saving your password in an environment variable.
For production, you might want to take info at the command line and
prompt for a password (without echoing) instead.
"""

import oeproxy
import os

class OEClientEnv(object):
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

    @property
    def url(self):
        """The URL set in the environment variable prefixURL"""
        return self._environ('URL')

    @property
    def dbname(self):
        """The database name set in the environment variable prefixDBNAME
        """
        return self._environ('DBNAME')

    @property
    def user(self):
        """The username set in the environment variable prefixUSER"""
        return self._environ('USER')

    @property
    def password(self):
        """The password set in the environment variable prefixPASSWORD
        """
        return self._environ('PASSWORD')

    def get_proxy(self):
        """Return a new OEProxy logged into the database configured in the
        environment.
        """
        oe = oeproxy.OEProxy(self.url)
        oe.login(self.dbname, self.user, self.password)
        return oe

    def get_erppeek_client(self, verbose=False):
        """Return a new erppeek.Client.

        Note you must have the erppeek package in the python path
        for this to work, or you will get an ImportError on call.
        """
        import erppeek
        return erppeek.Client(
            server=self.url,
            db=self.dbname,
            user=self.user,
            password=self.password,
            verbose=verbose
        )

    def _environ(self, suffix):
        """Return value of environment variable with given suffix."""
        return os.environ[self._var(suffix)]

    def _var(self, suffix):
        """Return the full environment variable name."""
        return self.prefix + suffix

__COPYRIGHT__ = """

This program is part of oekit: https://github.com/nmbooker/oekit

Copyright (c) 2015 Nicholas Booker <NMBooker@gmail.com>

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
