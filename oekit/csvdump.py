
"""A library to help with dumping out data from OpenERP models as CSV.

It's intended mostly for allowing you to get a quick view of the data in
a table while at a Python prompt, but you could us it in other programs
too.

I plan to include a generic command-line dumper script based on the
functionality in here.

The highest-level function you can use here is dump_csv.

Otherwise you can use a combination of:
    * one of get_all_rows, get_search_rows or get_rows
    * write_rows
"""

import csv
import sys

def dump_csv(oe_proxy, model, fields, ids=None, query=None, outfile=None):
    """Dump the model to outfile.

    oe_proxy: An OEProxy object to query.
    model: The name of the model to query.
    fields: The list of fields you want.
    ids: The ids you want.  'query' and 'ids' are mutually exclusive.
    query: If specified, an OpenERP ORM query.  If omitted, all records are fetched.
    outfile: If specified, a file-like object to write the CSV to.  If omitted, it's written to STDOUT.
    """
    if query and ids:
        raise ValueError('ids and query are mutually exclusive')
    if not query:
        query = []
    if not outfile:
        outfile = sys.stdout
    if ids is not None:
        rows = get_rows(oe_proxy, model, ids, fields)
    else:
        rows = get_search_rows(oe_proxy, model, query, fields)
    write_rows(outfile, rows)
    return

def get_all_rows(oe_proxy, model, fields):
    """Return all rows in the given model.

    oe_proxy: An OEProxy object.
    model: The name of the model to dump data from.
    fields: The list of fields names you want on each row.
    """
    return get_search_rows(oe_proxy, model, [], fields)

def get_search_rows(oe_proxy, model, query, fields):
    """Return all rows in the given model matching query.

    oe_proxy: An OEProxy object.
    model: The name of the model to dump data from.
    fields: The list of fields names you want on each row.
    """
    ids = oe_proxy.execute(model, 'search', query)
    return get_rows(oe_proxy, model, ids, fields)

def get_rows(oe_proxy, model, ids, fields):
    """Dump the given fields to a list of rows usable by
    csv.writer.writerow().

    oe_proxy: The OpenERP proxy object talking to your server.
    model: The name of the model to dump records from.
    ids: The ids of the records to dump.
    fields: The fields you want from those records.
    """
    schema = oe_proxy.execute(model, 'fields_get')
    records = oe_proxy.execute(model, 'read', ids, fields)
    rows = []
    rows.append(fields)
    for record in records:
        row = [_fixup_value(schema, field, record[field]) for field in fields]
        rows.append(row)
    return rows

def _cvtunicode(obj):
    if isinstance(obj, unicode):
        return obj.encode('utf-8')
    else:
        return obj

def _fixid(schema, field, obj):
    resolver = _value_resolver(schema, field, obj)
    return resolver.resolve(obj)

def _value_interpreter(schema, field, obj):
    if field == 'id':
        # doesn't sit in schema
        return SimpleValueInterpreter()
    elif schema[field]['type'] == 'one2many':
        return One2manyValueInterpreter()
    elif schema[field]['type'] == 'many2one':
        return Many2oneValueInterpreter()
    else:
        return SimpleValueInterpreter()

class SimpleValueInterpreter(object):
    def resolve(self, value):
        return value

class One2manyValueInterpreter(object):
    def resolve(self, value):
        return ';'.join(map(unicode, sorted(value)))

class Many2oneValueInterpreter(object):
    def resolve(self, value):
        return value[0] if value else None


def _fixup_value(schema, field, obj):
    return _fixid(schema, field, _cvtunicode(obj))

def write_rows(fileobj, rows):
    """Write the given rows as CSV to the given fileobj in default format.

    e.g.
    
    csv_write_rows(sys.stdout, [['name', 'email'], ['Fred', 'fred@example.org']]
    """
    writer = csv.writer(fileobj)
    for row in rows:
        writer.writerow(row)
    return

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
