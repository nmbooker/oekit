"""A simple proxy to an OpenERP server.

Author: Nick Booker
License: GPLv2

See __COPYRIGHT__ variable defined at bottom of the code.
"""

import xmlrpclib
from operator import itemgetter

class NotLoggedInError(Exception):
    pass

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
        if not self._uid:
            raise NotLoggedInError('not logged in - call login method first')
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

    def get_xmlid(self, xmlid):
        """Return model_name,res_id for the given XMLID.
        """
        (_, model, res_id) = self.execute('ir.model.data', 'xmlid_lookup', xmlid)
        return (model, res_id)



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

    def search(self, domain):
        """Return a list of ids of records matching domain.
        """
        return self.execute('search', domain)

    def read(self, ids, fields):
        """Return a list of dictionaries representing given ids.
        """
        return self.execute('read', ids, fields)


    def make_lookup_mapping(self, key_field, ids=None):
        """Return a dictionary mapping the given key field to an id.

        It's up to you to pick a key that is unique.

        key_field: The name of the field, e.g. 'code' or 'name'

        For example:
            odoo.get_model('res.country').make_lookup_mapping('code')

        That might return a dictionary looking something like this:
            {
                'GB': 1,
                'FR': 2,
                'IE': 3,
                ...
            }
        """
        if ids is None:
            ids = self.search([])
        records = self.read(ids, ['id', key_field])
        return {r[key_field]: r['id'] for r in records}

    def xmlids_of(self, res_ids):
        ids = self._oe.execute('ir.model.data', 'search', [('model', '=', self._model_name), ('res_id', 'in', res_ids)])
        recs = self._oe.execute('ir.model.data', 'read', ids, ['complete_name'])
        return map(itemgetter('complete_name'), recs)


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
