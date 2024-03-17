symbols = '$¢£¥€¤'
codes = []
for s in symbols:
    codes.append(ord(s))

print(codes)

# list comprehensions version

code = [ord(s) for s in symbols]

print(codes)

# ord(s) returns the ASCII code of the value passed as argument
x = 'ACB'

dummy = [ord(x) for x in x]

print(x, dummy)

# Listcomps versus map and filter, this was believed to be faster but it turns out not to

beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))

print(beyond_ascii)

# cartesian product or a matrix

colors = ['black', 'white']
sizes = ['S', 'M', 'L']

tshirts = [(c, s) for c in colors for s in sizes]

print('matrix', tshirts)

# generator expressions save up memory space when you need to init arrays, tuples and sequences in general

import array

print('tuple', tuple(ord(s) for s in symbols))

arr = array.array('I', tuple(ord(s) for s in symbols))
print(arr)

# magic function % helps format the test like old C
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)

# using the new .format()
for tshirt in ('{} {}'.format(c, s) for c in colors for s in sizes):
    print(tshirt)

# tuples are not only immutable lists but they can be also records with no field names

lax_coord = (44.3, 76.5)

traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

for passport in sorted(traveler_ids):
    print('{}'.format(passport))

# retrieving just one value
for city, _ in traveler_ids:
    print(city)

# tuples unpacking
city, year, pop, area = ('tokio', 2018, 32000, 8000)

for c in city:
    print(c)

# we can use it to swap var: b, a = a, b
t = (20, 8)

divmod(*t)

quotient, remainder = divmod(*t)
print(quotient, remainder)

# * grabs the excess items, it can be assigned to one variable in any positions
a, b, *rest = range(5)
print(rest)

# tuples can be nested

metro_ares = [('tokio', 'japanese', 34, (43.54, 32.42)), ('italy', 'italian', 22, (12.66, 67.5))]

print('{:15} | {:^9} | {:^9}'.format('name', 'lat', 'long'))

# named tuples are useful for naming the fields of a tuple

from collections import namedtuple

city = namedtuple('city', 'name country population coordinates')

tokyo = city('Tokyo', 'JP', 36.933, (35.689722, 139.691667))

print(tokyo, tokyo.name, tokyo[1], tokyo._fields)

LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))

# instance of names tuples
delhi = city._make(delhi_data)

# return a collections.OrderedDict
print(delhi._asdict())

for key, value in delhi._asdict().items():
    print(key + ':', value)

# slicing already saw in Python Crash Course.
"""
s = 'bicycle'

s[::3] 'bye'

s[::-1] 'elcycib'

s[::-2] 'eccb'

"""

# instead of hard coding slices I can name them as tuples

invoice = """
0.....6.................................40........52...55........
1909  Pimoroni PiBrella $17.50 3 $52.50
1489  6mm Tactile Switch x20 $4.95 2 $9.90
1510  Panavise Jr. - PV-201 $28.00 1 $28.00
1601  PiTFT Mini Kit 320x240 $34.95 1 $34.95 """

SKU = slice(0, 6)
DESCRIPTION = slice(6, None)

# cut in lines, excluding the first two lines
line_items = invoice.split('\n')[2:]
for item in line_items:
    print(item[SKU], item[DESCRIPTION])

l = list(range(10))

# the second and just to element 2+5
l[2::5] = [20, 30]
print(l)

# repeating a list items
m = [1, 2, 3]

m = m * 5

print(m)

# list od lists

board = [['_'] * 3 for i in range(3)]
print(board)

# *= or += are different effects on mutable and immutable sequences. after the mul a new tuple is created in
# a list instead just an append happened

# list.sort and the sorted built-in function: list.sort sort a list in place, instead the sorted method return a new
# list item regardless the type of the given iterable

fruits = ['grape', 'raspberry', 'apple', 'banana']
print(sorted(fruits, key=len))

fruits.sort()

# bisect has two modules: bisect e insort
# bisect module does a binary search

import sys
import bisect

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]
ROW_FMT = '{0:2d} @ {1:2d} {2}{0:<2d}'


def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        offset = position * ' |'
        print(ROW_FMT.format(needle, position, offset))


if __name__ == '__main__':
    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect
        print('DEMO:', bisect_fn.__name__)
        print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
        demo(bisect_fn)

# insort keeps the array sorted when you insert new items

# array in Python are still faster that list for storing numbers

from random import random
from array import array

floats = array('d', (random() for i in range(10**3)))

fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()

floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**3)
fp.close()

# for fast saving use the pickle module pickle.dump
# for sorting an array use the sorted function

a = array('I', (3,4,5,6,7,1,54,23,43))

a = array(a.typecode, sorted(a))

print(a)

# memoryview class built-in lets the handling slices of array without copying bytes

numbers = array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
print(len(memv))

# Cceate memv_oct by casting the elements of memv to typecode 'B' (unsigned char)
memv_oct = memv.cast('B')
memv_oct.tolist()
memv_oct[5] = 4

# NumPy and SciPy are useful libraries for numbers

# deques and other queues

from collections import deque
dq = deque(range(10), maxlen=10)
print(dq)

dq.rotate(3)
print(dq)

dq.appendleft(-1)
dq.extend([43, 54, 23])

print(dq)




