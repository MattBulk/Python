# With reference variables it makes much more sense to say that the variable is assigned to an object, and not the
# other way around. After all, the object is created before the assignment

"""
>>> x = Gizmo()
Gizmo id: 4301489152
>>> y = Gizmo() * 10
Gizmo id: 4301489432

"""

# always evaluate the right-hand side of the assignment, in the case shown the right side will thrown an error

charles = {'name': 'Charles L. Dodgson', 'born': 1832}

# lewis is an alias for charles.
lewis = charles

# this prints True
print(lewis is charles, id(charles), id(lewis))


alex = {'name': 'Charles L. Dodgson', 'born': 1832, 'balance': 950}

# this is True are dict
print(alex == charles)

# this is True cos are two different objects
print(alex is not charles)

# The is operator compares the identity of two objects; the id() function returns an integer representing its identity

# Choosing between == and is
# The == operator compares the values of objects (the data they hold), while is compares their identities

# The easiest way to copy a list (or most built-in mutable collections) is to use the builtin constructor for the
# type itself, for example:

l1 = [3, [5,6], (7,8,9)]
l2 = list(l1)

print(l1, l2)

# For lists and other mutable sequences, the shortcut l2 = l1[:] also makes a copy

# Deep and shallow copies of arbitrary objects
# The copy module provides the deepcopy and copy functions that return deep and shallow copies of arbitrary objects

# del and garbage collection and Weak references
"""

The del statement deletes names, not objects. An object may be garbage collected as result of a del command, 
but only if the variable deleted holds the last reference to the object, or if the object becomes unreachable4. 
Rebinding a variable may also cause the number of references to an object reach zero, causing its destruction.

Weak references to an object do not increase its reference count. The object that is the target of a reference is 
called the referent. Therefore, we say that a weak reference does not prevent the referent from being garbage collected

"""

import weakref

# A weak reference is a callable that returns the referenced object or None if the referent is no more

a_set = {0, 1}
wref = weakref.ref(a_set)

print(wref)

# Object Representations :

# repr() Return a string representing the object as the developer wants to see it
# str() Return a string representing the object as the user wants to see it

# classmethod versus staticmethod

# classmethod: to define a method that operates on the class and not in instances. it changes the way the method is
# called, so it receives the class itself as the first argument, instead of an instance. Its most common use is for
# alternate constructors.

# the staticmethod decorator changes a method so that it receives no special first argument. In essence, a static method
#  is just like a plain function that happens to live in a class body, instead of being defined at the module level.


class Demo:

    @classmethod
    def klassmeth(*args):
        return args

    @staticmethod
    def statmeth(*args):
        return args


print(Demo.klassmeth())
# No matter how you invoke it, Demo.klassmeth receives the Demo class as the first argument.
print(Demo.klassmeth('spam'))

# Demo.statmeth behaves just like a plain old function.
print(Demo.statmeth())
print(Demo.statmeth('spam'))

# Private and “protected” attributes

"""
To prevent this, if you name an instance attribute in the form __mood (two leading underscores and zero or at most one
trailing underscore), Python stores the name in the instance __dict__ prefixed with a leading underscore and the class 
name, so in the Dog class, __mood becomes _Dog__mood, and in Beagle it’s _Beagle__mood. This languagefeature goes by 
the lovely name of name mangling.
"""

# Saving space with the __slots__ class attribute

"""
By default, Python stores instance attributes in a per-instance dict named __dict__. As we saw in “Practical 
consequences of how dict works” on page 90, dictionaries havea significant memory overhead because of the underlying 
hash table used to provide fast access. If you are dealing with millions of instances with few attributes, the
__slots__ class attribute can save a lot of memory, by letting the interpreter store the instance attributes in a tuple 
instead of a dict.

If you are handling millions of objects with numeric data, you should really be using NumPy arrays, which are not only 
memory-efficient but have highly optimized functions for numeric processing, many of which operate on the entire array 
at once.
"""

# Overriding class attributes

# v1 = Vector2d(1.1, 2.2)
# v1.typecode = 'f'

# Vector2d.typecode is still the default 'd'
























# chapter 10 is quite useless an implementation of Vectors, nothing more
