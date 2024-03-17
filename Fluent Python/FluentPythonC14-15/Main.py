# the iter function
# the interpreter automatically calls iter(x):

"""
The iter built-in function:
1. Checks whether the object implements, __iter__, and calls that to obtain an iterator;
2. If __iter__ is not implemented, but __getitem__ is implemented, Python creates
an iterator that attempts to fetch items in order, starting from index 0 (zero);
3. If that fails, Python raises TypeError, usually saying "'C' object is not iterable",
where C is the class of the target object.

in the future __getitem__ couldn't be present, present now for backward compatibility

"""

# Iterables versus iterators

"""
iterable
Any object from which the iter built-in function can obtain an iterator. Objects
implementing an __iter__ method returning an iterator are iterable. Sequences
are always iterable; so as are objects implementing a __getitem__ method which
takes 0-based indexes.

>>> s = 'ABC'
>>> for char in s:
... print(char)
...
A
B
C

this is what happen under the curtains:

>>> s = 'ABC'
>>> it = iter(s) #
>>> while True:
...     try:
...         print(next(it)) #
...     except StopIteration: #
...         del it #
...         break

"""

# the standard interface has two method :
# next : return the next available item, raising StopIteration
# iter : return self this allows iterators to be used where an iterable is expected, for example, in a for loop

"""
A common cause of errors in building iterables and iterators is to confuse the two. To
be clear: iterables have a __iter__ method that instantiates a new iterator every time.
Iterators implement a __next__ method that returns individual items, and a __iter__
method that returns self.
Therefore, iterators are also iterable, but iterables are not iterators.
"""

# check itertools and os.walk

# New syntax in Python 3.3: yield from


def chain(*iterables):
    for it in iterables:
        for i in it:
            yield i


s = 'ABC'
t = tuple(range(3))
print(list(chain(s, t)))

# new version


def chain(*iterables):
    for i in iterables:
        yield from i


print(list(chain(s, t)))

# from replaces the inner loop
"""
Besides replacing a loop, yield from creates a channel connecting the inner
generator directly to the client of the outer generator. This channel becomes really important
when generators are used as coroutines and not only produce but also consume
values from the client code.
"""

"""
Iterable reducing functions page 437
The functions in Table 14-6 all take an iterable and return a single result. They are known
as “reducing”, “folding” or “accumulating” functions.
"""

# chapter 15
"""
The two method are:
• The with statement and context managers.
• The else clause in for, while and try statements.

Context manager objects exist to control a with statement, just like iterators exist to
control a for statement.
The with statement was designed to simplify the try/finally pattern which guarantees
that some operation is performed after a block of code, even if the block is aborted
because of an exception, a return or sys.exit() call. The code in the finally clause
usually releases a critical resource or restores some previous state that was temporarily
changed.
The context manager protocol consists of the __enter__ and __exit__ methods. At the
start of the with, __enter__ is invoked on the context manager object. The role of the
finally clause is played by a call to __exit__ on the context manager object at the end
of the with block.

When control flow exits the with block in any way, the __exit__ method is invoked on
the context manager object, not on whatever is returned by __enter__.
"""

"""
Using @contextmanager
The @contextmanager decorator reduces the boilerplate of creating a context manager:
instead of writing a whole class with __enter__/__exit__ methods, you just implement
a generator with a single yield that should produce whatever you want the __en
ter__ method to return.
In a generator decorated with @contextmanager, yield is used to split the body of the
function in two parts: everything before the yield will be executed at the beginning of
the while block when the interpreter calls __enter__; the code after yield will run
when __exit__ is called at the end of the block.
"""

# http://www.zopatista.com/python/2013/11/26/inplace-file-rewriting/
