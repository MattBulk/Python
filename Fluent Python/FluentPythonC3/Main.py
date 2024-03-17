# dictionary

DIAL_CODES = [

(86, 'China'),
(91, 'India'),
(1, 'United States'),
(62, 'Indonesia'),
(55, 'Brazil'),
(92, 'Pakistan'),
(880, 'Bangladesh'),
(234, 'Nigeria'),
(7, 'Russia'),
(81, 'Japan'),
]


country_code = {country: code for code, country in DIAL_CODES}

# check dict.setdefault and collections.defaultdict

# the __missing__ method

from StrKeyDict0 import *

d = StrKeyDict0([('2', 'two'), ('4', 'four')])

print(d['2'], d.get(4))

# variations of dict

# collections.OrderedDict : maintains keys in insertion order

# collections.ChainMap : holds a list of mappings which can be searched as one. See docs for examples

import builtins
from collections import  ChainMap, Counter

pylookup = ChainMap(locals(), globals(), vars(builtins))
print(pylookup)

# collections.Counter : a mapping that holds an integer count for each key

ct = Counter('superSpottedHype')
print(ct)

# collections.UserDict pure implementation of a mapping like a standard dict, but needs to be subclassed
# see StrKeyDict.py class

# immutable mappings are possible thanks to MappingProxyType that returns a read-only instance

from types import MappingProxyType

d = {1: 'A'}
d_proxy = MappingProxyType(d)

# for updating d_proxy the only way is to update d otherwise a TypeError will be thrown
d[2] = 'B'
print(d_proxy)

# sets are collections of unique items

l = ['spam', 'spam', 'eggs', 'spam']
print(set(l))

# if needles and haystack are set we can use the first simple method len

"""
found = len(needles & haystack)

instead of 

found = 0
    for n in needles:
        if n in haystack:
            found += 1
"""

# found = len(set(needles) & set(haystack)) WORKS FOR ANY KIND OF ITERABLE TYPES

# set literals

s = {1, 2, 3}
print(type(s))

# frozenset
frozenset(range(10))

# set comprehensions
# d = {chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i),'')}

# check the book for the reason why dict and set are so fast (hashing)
