
"""OpenERP client using environment variables for logging in.

This allows you to write quick and dirty test scripts.

I wouldn't consider it secure for writing production scripts because
it involves saving your password in an environment variable.
For production, you might want to take info at the command line and
prompt for a password (without echoing) instead.
"""

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

    def _environ(self, suffix):
        """Return value of environment variable with given suffix."""
        return os.environ[self._var(suffix)]

    def _var(self, suffix):
        """Return the full environment variable name."""
        return self.prefix + suffix


__COPYRIGHT__ = """The MIT License (MIT)

Copyright (c) 2013 Nicholas Booker <NMBooker@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

