# encoding and decoding

s = 'cafè'
print(len(s))

# è is the char chosen to show the encoding that is not in the ASCII range
b = s.encode('utf8')
print(b, len(b))

# decoding making readable to humans
b = b.decode('utf8')
print(b)

# 5 byte sequence as bytes and as bytearray

# bytes built from a str
cafe = bytes('cafè', encoding='utf8')

# print char as INT and slice it as byte
print(cafe[0], cafe[:1])

cafe_arr = bytearray(cafe)
print(cafe_arr, cafe_arr[-1:])

# binary in HEX
bytes.fromhex('31 4B CE A9')

# this way we can copy an array in bytes, instead memoryview will share the same memory
import array
numbers = array.array('h', [-2, -1, 0, 1, 2])
octets = bytes(numbers)

# struct and memoryview
# using memoryview and struct to inspect a GIF image header.
import struct

# struct format: < little-endian; 3s3s two sequences of 3 bytes; HH two 16-bit integers,
fmt = '<3s3sHH'
with open('giphy.gif', 'rb') as fp:
    img = memoryview(fp.read())

# with no copied bytes I created another memoryview
header = img[:10]
bytes(header)

struct.unpack(fmt, header)

# deleting references to release
del header
del img

# Handling code/decode problems when we convert not char defined in the charset, so that a UnicodeEncodeError is shown
# the same happens with UnicodeDecodeError
# SyntaxError are raised when loading modules containing non-UTF-8 code

# handling text files
# the Unicode sandwich is a best practice that decodes bytes to str asap. Python has got a built-in method for it

open('cafe.txt', 'w', encoding='utf_8').write('café')

print(open('cafe.txt').read())

# normalize unicode for saner string comparisons
from unicodedata import normalize, name

s1 = 'cafè'
s2 = 'cafe\u0301'
print(len(s1), len(s2), s1 == s2)

# unicodedata.normalize 'NFC' 'NFD' 'FNKC' 'NFKD'

# NFC composes the shortest equivalent string
print(len(normalize('NFC', s1)), len(normalize('NFC', s2)), s1 == s2)

# NFD decomposes and expands the chars
print(len(normalize('NFD', s1)), len(normalize('NFD', s2)), s1 == s2)

# K in the other two forms stands for compatibility but they can lose of distort information

half = '½'
print(normalize('NFKC', half))

# str.casefold() works like str.lower() with a major impact with languages different tha latin1
# diacritics are accents, cedillas; they can be removed like this:

import unicodedata
import string


def shave_marks(txt):
    """Remove all diacritic marks"""
    norm_txt = unicodedata.normalize('NFD', txt)
    shaved = ''.join(c for c in norm_txt if not unicodedata.combining(c))

    return unicodedata.normalize('NFC', shaved)

# sorting unicode is made simple by passing local.strxfrm but it is important di not set locale locally in the libs
# locale must be installed correctly on the OS or error are raised
# the right spell for the locale "United States" "English" ...


import locale

print(locale.setlocale(locale.LC_COLLATE, 'pt_BR.UTF-8'))

fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']

sorted_fruits = sorted(fruits, key=locale.strxfrm)
print(sorted_fruits)

# a better solution is given by the PyPI lib
"""
import pyuca
coll = pyuca.Collator()
fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']
sorted_fruits = sorted(fruits, key=coll.sort_key)
sorted_fruits
"""

# the Unicode database records whether a character is printable, is a letter, is a decimal digit or is some other
# numeric symbol. That’s how the str methods isidentifier, isprintable, isdecimal and isnumeric work. str.casefold
# also uses information from a Unicode table.

# str versus bytes in regular expressions

import re, os

# str
re_numbers_str = re.compile(r'\d+')
re_words_str = re.compile(r'\w+')
# bytes
re_numbers_bytes = re.compile(rb'\d+')
re_words_bytes = re.compile(rb'\w+')

text_str = "Ramanujan saw \u0be7\u0bed\u0be8\u0bef as 1729 = 1³ + 12³ = 9³ + 10³."
text_bytes = text_str.encode('utf_8')

print('Text', repr(text_str), sep='\n ')
print('Numbers')
print(' str :', re_numbers_str.findall(text_str))
print(' bytes:', re_numbers_bytes.findall(text_bytes))
print('Words')
print(' str :', re_words_str.findall(text_str))
print(' bytes:', re_words_bytes.findall(text_bytes))


os.listdir('.')  # ['abc.txt', 'digits-of-π.txt']

os.listdir(b'.')  # [b'abc.txt', b'digits-of-\xcf\x80.txt']

