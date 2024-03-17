def factorial(n):
    """return n!"""
    return 1 if n<2 else n * factorial(n-1)


f = factorial(10)

# __doc__ prints the comment in """"""

print(f, factorial.__doc__)

# create a map of all the calls to the function, this is an higher-order function cos it takes a function as args

list = list(map(factorial, range(10)))

print(list)

# we can do the same with list comprehensions, maps and filters in Python3 return generators

list = [factorial(n) for n in range(6) if n % 2]

# The common idea of sum and reduce is to apply some operation to successive items in a sequence, accumulating
# previous results, thus reducing a sequence of values to a single value

from functools import reduce
from operator import add

reduce(add, range(100))

sum(range(100))

# anonymous functions are limited to pure expressions but are very limited to use

#

