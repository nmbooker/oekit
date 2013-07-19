
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

def dump_csv(oe_proxy, model, fields, query=None, outfile=None):
    """Dump the model to outfile.

    oe_proxy: An OEProxy object to query.
    model: The name of the model to query.
    fields: The list of fields you want.
    query: If specified, an OpenERP ORM query.  If omitted, all records are fetched.
    outfile: If specified, a file-like object to write the CSV to.  If omitted, it's written to STDOUT.
    """
    if not query:
        query = []
    if not outfile:
        outfile = sys.stdout
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
    records = oe_proxy.execute(model, 'read', ids, fields)
    rows = []
    rows.append(fields)
    for record in records:
        row = [_fixup_value(record[field]) for field in fields]
        rows.append(row)
    return rows

def _cvtunicode(obj):
    if isinstance(obj, unicode):
        return obj.encode('utf-8')
    else:
        return obj

def _fixid(obj):
    if isinstance(obj, list):
        return obj[0]   # this would be the id in an [id, string] pair
    else:
        return obj

def _fixup_value(obj):
    return _fixid(_cvtunicode(obj))

def write_rows(fileobj, rows):
    """Write the given rows as CSV to the given fileobj in default format.

    e.g.
    
    csv_write_rows(sys.stdout, [['name', 'email'], ['Fred', 'fred@example.org']]
    """
    writer = csv.writer(fileobj)
    for row in rows:
        writer.writerow(row)
    return

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

