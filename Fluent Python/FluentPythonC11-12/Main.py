# interfaces and protocols in Python

# NOTE on duck-typing https://stackoverflow.com/questions/4205130/what-is-duck-typing

"""
the basics: even without
an interface keyword in the language, and regardless of ABCs, every class has an interface: the set public attributes
(methods or data attributes) implemented or inherited by the class. This includes special methods,
like __getitem__ or __add__.

By definition, protected and private attributes are not part of an interface, even if “protected” is merely a naming
convention (the single leading underscore) and private attributes are easily accessed

A useful complementary definition of interface is: the subset of an object’s public methods that enable it to play
a specific role in the system. That’s what is implied when the Python documentation mentions “a file-like object”
or “an iterable”, without specifying a class. An interface seen as a set of methods to fulfill a role is what
Smalltalkers called a procotol, and the term spread to other dynamic language communities. Protocols are independent
of inheritance. A class may implement several protocols, enabling its instances to fulfill several roles.

Protocols are interfaces, but because they are informal — defined only by documentation and conventions — protocols
cannot be enforced like formal interfaces can (we’ll see how ABCs enforce interface conformance later in this chapter).
A protocol may be partially implemented in a particular class, and that’s OK. Sometimes all a specific API requires
from “a file-like object” is that it has a .read() method that returns bytes. The remaining file methods may or may not
be relevant in the context.

"""

# subclassing an ABC : see frenchdeck2.py

# Tombola.py

"""
The point of this example is to highlight that it’s OK to
provide concrete methods in ABCs, as long as they only depend on other methods in
the interface. Being aware of their internal data structures, concrete subclasses of Tom
bola may always override .inspect() with a smarter implementation, but they don’t
have to.
"""

# A virtual subclass of Tombola

"""
An essential characteristic of goose typing — and the reason why it deserves a waterfowl
name — is the ability to register a class as a virtual subclass of an ABC, even if it does
not inherit from it. When doing so, we promise that the class faithfully implements the
interface defined in the ABC — and Python will believe us without checking. If we lie,
we’ll be caught by the usual runtime exceptions.
This is done by calling a register method on the ABC. The registered class then becomes
a virtual subclass of the ABC, and will be recognized as such by functions like
issubclass and isinstance, but it will not inherit any methods or attributes from the
ABC.
"""

# Usage of register in practice

"""
even if register can now be used as a decorator, it’s more widely deployed
as a function to register classes defined elsewhere. For example, in the source code for
the collections.abc module, the built-in types tuple, str, range and memoryview are
registered as virtual subclasses of Sequence like this:
Sequence.register(tuple)
Sequence.register(str)
Sequence.register(range)
Sequence.register(memoryview)
"""

# Chapter 12
"""
This chapter is about inheritance and subclassing, with emphasis on two particulars
that are very specific to Python:
• The pitfalls of subclassing from built-in types.
• Multiple inheritance and the method resolution order.

Multiple inheritance and method resolution order

Any language implementing multiple inheritance needs to deal with potential naming
conflicts when unrelated ancestor classes implement a method by the same name. This
is called the “diamond problem” : check page 353
"""

class A:
    def ping(self):
        print('ping:', self)


class B(A):
    def pong(self):
        print('pong:', self)


class C(A):
    def pong(self):
        print('PONG:', self)


class D(B, C):
    def ping(self):
        super().ping()
        print('post-ping', self)

    def pingpong(self):
        self.ping()
        super().ping()
        self.pong()
        super().pong()
        C.pong(self)


d = D()
print(d.pong(), C.pong(d))
print(D.__mro__)

"""
the most visible use of multiple inheritance is the col
lections.abc package. That is not controversial: after all, even Java supports multiple
inheritance of interfaces, and ABCs are interface declarations which may optionally
provide concrete method implementations
"""

# check mixin classes page 361 - 362

# chapter 13

# Overloading + for vector addition


v1 = list([3, 4, 5, 6])
v3 = list([1, 2])

# it appends v3 to v1
print(v1 + v3)

"""
>>> v1 = Vector([3, 4, 5, 6])
>>> v3 = Vector([1, 2])
>>> v1 + v3
Vector([4.0, 6.0, 5.0, 6.0])
"""

# flowchart 379








