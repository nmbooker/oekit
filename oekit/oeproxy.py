"""A simple proxy to an OpenERP server.

Author: Nick Booker
License: MIT License

See __COPYRIGHT__ variable defined at bottom of the code.
"""

import xmlrpclib

class OEProxy(object):
    """OpenERP Proxy Client

    oe = OEProxy('http://localhost:8069')
    oe.login('mydb', 'username', 'password')
    partner_model = oe.get_model('res.partner')
    ids = partner_model.execute('search', [])
    partners = partner_model.execute('read', ids)
    """
    def __init__(self, url):
        """
        url: The URL of the OpenERP XML-RPC interface, e.g. http://localhost:8069
        """
        self._url = url
        self._uid = None
        self._dbname = None
        self._user = None
        self._password = None
        self._sock_common = xmlrpclib.ServerProxy(url + '/xmlrpc/common')
        self._sock = xmlrpclib.ServerProxy(url + '/xmlrpc/object')

    def login(self, dbname, user, password):
        """Log into the server.
        """
        self._uid = self._sock_common.login(dbname, user, password)
        self._dbname = dbname
        self._user = user
        self._password = password
        return

    def execute(self, model_name, method_name, *args):
        """Execute a method on the server you logged into.

        model_name: The name of the OpenERP model.
        method_name: The name of the method to call on that model.
        args: The arguments (positional) to pass to the method.
        """
        result = self._sock.execute(
            self._dbname,
            self._uid,
            self._password,
            model_name,
            method_name,
            *args
        )
        return result

    def get_model(self, model_name):
        """Return a proxy that fills in model_name for you on all methods.

        model_name: The model name you want to emulate.
        """
        return OEModelProxy(self, model_name)


class OEModelProxy(object):
    """Proxies an OpenERP model.

    Use OEProxy.get_model method to instantiate this.
    """
    def __init__(self, oe_proxy, model_name):
        self._oe = oe_proxy
        self._model_name = model_name

    def execute(self, method_name, *args):
        """Call the given method on the wrapped model.

        method_name: The name of the method to call.
        args: The arguments you want to pass that method.
        """
        return self._oe.execute(self._model_name, method_name, *args)

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
