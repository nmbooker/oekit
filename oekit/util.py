#!/usr/bin/env python

"""Generic utilities developed for use in oekit.

TODO: Move these into python-funbox
"""

def ext_wildcard(ext):
    """
    >>> ext_wildcard('png')
    '*.png'
    """
    return '*.%s' % (ext,)

def join_iters(separator, sequences):
    """
    >>> list(join_iters(8, []))
    []
    >>> list(join_iters(8, [['a', 'b']]))
    ['a', 'b']
    >>> list(join_iters(8, [['a', 'b'], ['c', 'd']]))
    ['a', 'b', 8, 'c', 'd']
    """
    for (i, xs) in enumerate(sequences):
        if i > 0:
            yield separator
        for x in xs:
            yield x


if __name__ == "__main__":
    import doctest
    doctest.testmod()
