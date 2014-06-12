# -*- coding: utf-8 -*-
# Copyright (c) 2014 Vladimir Chub
# All rights reserved.
#
# This software is licensed as described in the file LICENSE, which
# you should have received as part of this distribution.
#
# Author: Vladimir Chub

"""
TUVAN TOOLS. Yet another python toolkit.
"""

__author__ = 'Vladimir Chub'
__email__ = 'vartagg@users.noreply.github.com'
__version__ = '0.1.0'


def dict_slice(dict_, keys, default_value=None, strict=False):
    """
    Returns a part of dictionary dict_ containing the keys

    :param default_value: The value to be assigned to key that cannot be found in the dictionary _dict
    :param strict: If True and dict_ cannot accessed to some key from keys, KeyError will be raised. Default: False

    >>> a = {'x': 1, 'y': 2, 'z': 3}
    >>> dict_slice(a, ['x', 'y'])
    {'y': 2, 'x': 1}
    >>> b = {'y': 2, 'z': 3}
    >>> dict_slice(b, ['x', 'y'])
    {'y': 2, 'x': None}
    >>> dict_slice(b, ['x', 'y'], 'donut hole')
    {'y': 2, 'x': 'donut hole'}
    >>> dict_slice(b, ['x', 'y'], strict=True) # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    KeyError: 'x'
    """
    fn = (lambda k: dict_.get(k, default_value)) if not strict else (lambda k: dict_[k])
    return {k: fn(k) for k in keys}


def dict_besides(dict_, keys):
    """
    Returns a part of dictionary dict_ not containing the keys

    >>> a = {'x': 1, 'y': 2, 'z': 3, 'z1': 4}
    >>> dict_besides(a, ['x', 'y'])
    {'z': 3, 'z1': 4}
    >>> dict_besides(dict(), ['x', 'y'])
    {}
    """
    return {k: dict_.get(k) for k in dict_ if k not in keys}


def are_unique(seq):
    """
    Returns True if elements in seq are unique, and False otherwise

    >>> are_unique([1, 2, 3])
    True
    >>> are_unique([1, 2, 3, 2])
    False
    >>> are_unique([])
    True
    """
    seen = set()
    return not any(elem in seen or seen.add(elem) for elem in seq)


def dicts_union(dict1, dict2, strict=False):
    """
    Returns the union of two dictionaries

    :param strict: If True and keys of dictionaries are intersected, KeyError will be raised. Default: False

    >>> dicts_union({'x': 'temp', 'y': 'foo'}, {'z': 'bar'}) == {'y': 'foo', 'x': 'temp', 'z': 'bar'}
    True
    >>> dicts_union({'x': 'temp', 'y': 'foo'}, {'x': 'bar'}) == {'y': 'foo', 'x': 'bar'}
    True
    >>> dicts_union({'x': 'temp', 'y': 'foo'}, {'x': 'not temp'}, True) # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    KeyError: Some keys of dicts are intersected
    """
    items = dict1.items() + dict2.items()
    if strict and not are_unique([item[0] for item in items]):
        raise KeyError('Some keys of dicts are intersected')
    return dict(items)


def raise_function(exc):
    """
    Helps raise custom exceptions inside lambdas

    >>> foo = lambda x: x != 13 or raise_function(ValueError('Suddenly'))
    >>> foo(13) # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    ValueError: Suddenly
    """
    raise exc


def each(callback, items):
    """
    >>> bar_list = []
    >>> foo_list = [i for i in range(9)]
    >>> each(lambda x: bar_list.append(x*3), foo_list)
    >>> bar_list
    [0, 3, 6, 9, 12, 15, 18, 21, 24]
    """
    for item in items:
        callback(item)


def chunks(l, n):
    """
    >>> a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> [i for i in chunks(a, 5)]
    [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
    >>> [i for i in chunks(a, 4)]
    [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9]]
    """
    for i in xrange(0, len(l), n):
        yield l[i:i+n]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
