# a decorator is a callable that takes another function as argument (the decorated function)
# the first crucial fact about decorators is that they have the power to replace the decorated function
# with a different one. The second crucial fact is that they are executed immediately when a module is loaded.


from registration import *

main()


# Most decorators do change the decorated function. They usually do it by defining an inner function and returning
# it to replace the decorated function. Code that uses inner functions almost always depends on closures to operate
# correctly. To understand closures we need to understand var scopes.


# when Python compiles the body of the function, it decides that b is a local variable because it is assigned
# within the function, the next example thrown an error
"""
b = 6

>>> def f2(a):
... print(a)
... print(b)
... b = 9

"""

# do define a var global we need to define it as : global b !

# closures
# closures only matter when you have nested functions.

import average

average.avg(12)

def make_averager():
    #closure
    series = []

    def averager(new_value):
        # series is the free var, this mean the var is not bound in the local scope
        series.append(new_value)
        total = sum(series)
        return total/len(series)

    return averager


# a closure is function that retains the bindings of the free variables that exist when the function is defined,
# so that they can be used later when the function is invoked and the defining scope is no longer available

# To work around this the nonlocal declaration was introduced in Python 3. It lets you flag a variable as a free
# variable even when it is assigned a new value within the function

def make_averager2():
    count = 0
    total = 0

    def averager2(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count
    return averager2


# clocked demo page 197 ! nice example

# Python has three built-in functions that are designed to decorate methods: property, classmethod and staticmethod

# Another frequently seen decorator is functools.wraps, a helper for building wellbehaved decorators

# decorators can be stacked
"""
@d1
@d2
def f():
    print('f')

"""

# Parametrized Decorators simply args can be passed

"""
@register(active=False)
def f1():
    print('running f1()')

@clock('{name}: {elapsed}s')
def snooze(seconds):
    time.sleep(seconds)

"""
