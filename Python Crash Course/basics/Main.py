
# generators

def generator():
    for i in range(6):
        yield i*i

# uso di yield serve per evitare di dover processare e tenere in memoria dati
# yield ritorna il valore e poi ferma il metodo generator modificato
g = generator()
for i in g:
    print(i)


# ------------------------------- Python Crash Course --------------------------------

favorite_language = 'python '
print(favorite_language)

# this removes the strips forever
# r and l strip stand for right and left if you need to strip whitespaces
# strip removes from both sides
favorite_language = favorite_language.rstrip()
print(favorite_language)

name = 'eric wayne'
print('Hello ' + name + ', would you like to learn some Python today?')
print(name.lower() , name.upper(), name.title())

print('Albert Einstein once said, "A person who never made a mistake never tried anything new."')

# ** it is used ad exponential
# operations are executed in order, so you need parenthesis
exp = 3 ** 3
print('exp', exp)

# str() is the toString method
age = 36
birthday = 'The 22 of July 2017 I have turned ' + str(age)
print(birthday)

# ------------------------------- 3 LIST --------------------------------
# list ar arrays similar to as3, they can contain different types of objects
bicycles = ['treck', 'mtb', 'redline', 43]
print(bicycles)

# the last element of the list is -1
print(bicycles[-1])

# append does add an element to the end of a list
# insert does insert an element to a certain index
# del removes the item
bicycles.append(birthday)
bicycles.insert(2, 'racer')
print(bicycles)

del bicycles[5]
print(bicycles)

# pop removes the last element of a list, if a index is passed it removes the element ad that index
the_only_number = bicycles.pop()
the_mtb = bicycles.pop(1)
print(the_only_number, the_mtb)

# remove(value) value can also be a variable, it removes just the first one in case of multiple cases...
bicycles.remove('racer')
print(bicycles)

# lists have sort method sort(reverse=true)
bicycles.append('boto')
bicycles.append('mtb')
bicycles.sort(reverse=True)
print(bicycles)

# sorted presents just the list ordered but it does not affect the real order
# reverse rearrange the list upside down
# len(list)
bicycles.reverse()
print(bicycles, len(bicycles))

# ------------------------------- 4 WORKING WITH LIST --------------------------------

magicians = ['Alice', 'David', 'Nicola']
for mag in magicians:
    print(mag)

# range(n, n) is used as the classic for loop C, Java... and can be even used to generate a list
numbers = list(range(1, 8))

# starting from 2 it prints even number by the increment
even_numbers = list(range( 2, 21, 2))
print(even_numbers)

# useful method: min() max() sum()
# list comprehensions it create a list thanks to a loop
squares = [value**2 for value in range(1,11)]
print(squares)

# slicing a list [n:n]
# [:n] it starts from the beginning
# [n:] to the end
# in can be used to loop through a part of a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

# copying a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

# instead be aware of this: this let friend_food point to my_foods
friend_foods = my_foods
my_foods.append('pasta')
print(friend_foods)

# tuple are similar to set of constants. These are defined like a list
dimension = (20, 500)
print(dimension[0], dimension[1])
# to modify the tuple you need to declare them again
dimension = (400, 300)

# ------------------------------- 5 IF STATEMENT --------------------------------

# just like any other languages just the use of && || != in Python is and or not

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")

# else if = elif and I can omit the last else statement in a chain
# in case of empty list the if test return false
requested_toppings = []
if requested_toppings:
    print('serve it')
else:
    print("Are you sure you want a plain pizza?")

# if can be used to check if a value is in one other list
# if requested_topping in available_toppings:

# ------------------------------- 6 DICTIONARY --------------------------------

# a dic stored elements and key values color is the key green the value, very similar di Structs in C/C++
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

# add keys to dictionary is easy, the book says dictionary doesnt care about order of adding keys

alien_0['x_pos'] = 20
alien_0['y_pos'] = 0

print(alien_0)

del alien_0['points']

# for looping inside a dictionary
# .keys() is the default looping option

for key, value in alien_0.items():
    print('\nKey: ' + key)
    print('Value: ' + str(value))

# .values() loops inside the values of the dict
# to eliminate repeating elements we can use set()
for v in set(alien_0.values()):
    print('\nKey: ' + key)
    print('Value: ' + str(value))

# dicts can be nested in lists and likewise we can put list into dicts
# Store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

# this way I can access an element in the list
new_pizza = pizza['toppings']
print(new_pizza[0])

# I can nest dicts into dicts, but not very good practice

# ------------------------------- 7 INPUT --------------------------------

# need to convert string to int when input numbers int(message)
# message = input("Tell me something nice: \n")
# print(message)

# while loop
current_num = 0
while current_num <= 5:
    print(current_num)
    current_num += 1

# the others uses of while loop are the same, quit, use a boolean as flag, break and continue
# nice way to move object from list or dicts:
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

# remove items into a list
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']

while 'cat' in pets:
    pets.remove('cat')
print(pets)

# ------------------------------- 8 FUNCTION --------------------------------

# function works similar to Java ... some examples
# using default values in the arguments b can end up mix the positional parameters


def first_fun(a, b=9):

    c = a + b
    return c


x = first_fun(4, 3)
y = first_fun(a=12, b=34)
z = first_fun(2)
print(x, y, z)

# defining optional arguments :
# def first_fun(a, b=9, c=''):

# preventing a function from modifying a list by passing a copy of the list itself
"function_name(list_name[:])"



# **args lets add different numbers of arguments


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    # dict literal
    profile = {
        'first_name': first,
        'last_name': last
    }
    for k, value in user_info.items():
        profile[k] = value
    return profile


user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)

# we can store functions into modules

import pizza

pizza.make_pizza('pepperoni')


pizza.make_pizza('mushrooms', 'green peppers', 'extra cheese')

# importing specific functions with:
"""from module_name import function_0, function_1, function_2"""

from pizza import make_pizza

make_pizza('mozzarella', 'salami')

# add as to make an alias : from pizza import make_pizza as mp for instance
# * imports all the function from a module


# ------------------------------- 9 CLASSES --------------------------------

class ExampleClass(object):
    # the init method is the Java ClassNameMethod
    def __init__(self, n, surname, email):
        self.n = n
        # The "dunder" (double underscore, __) prefix prevents access to attribute, except through accessors.
        self.__surname = surname
        self.email = email

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value):
        self.__surname = value

# setting property e setter I have just implemented getter/setter private attributes like Java


i = ExampleClass('matteo', 'bulgarelli', 'mistakenness@gmail.com')

print(i.surname)
i.surname = 'Govi'

print(i.surname)

from MyFirstClass import MyFirstClass

my_array = []

for l in range(1, 5):
    y = MyFirstClass(7, 'ala')
    y.my_class_method()
    my_array.append(y)

from MyFirstInHer import *
o = MyFirstInHer(7, 'attack', 'fiorentina')
print(o.team_name)
o.my_class_method()

# in one module (class.py) can be stored multiple classes so I can choose which one to import

# ------------------------------- 10 FILES AND EXCEPTIONS --------------------------------


# writing a file w to write a for append
with open('instance.txt', 'w') as myFile:
    for m in range(1,5):
        myFile.write('Hello! ')

# the book says it should be a whitespace at the end of the file. I dont see it in the output
with open('instance.txt', 'r') as myFile:
    print(myFile.read())

# the path are store in different ways:
# Linux and OSX : file_path = '/home/ehmatthes/other_files/text_files/filename.txt'
# Windozzz : file_path = 'C:\Users\ehmatthes\other_files\text_files\filename.txt'

# looping with a for loop for reading line by line
with open('instance.txt', 'r') as myFile:
    for lines in myFile:
        print(lines)

# create a list of lines:
with open('instance.txt', 'r') as myFile:
    lines = myFile.readlines()

# exception example: I can check the case of file not found
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# split() method just like Java
# pass keywords lets passing silently through a failing

"""try:
    --snip--
except FileNotFoundError:
    pass
else:
    --snip--
"""
# storing data in json dump() let us write
import json

numbers = [2, 4, 33, 65, 12, 6]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)

with open(filename, 'r') as f_obj:
    numbers = json.load(f_obj)

print(numbers)

# ------------------------------- 11 TESTING --------------------------------

# Python gives us unittest.TestCase class an assert class
"""
assertEqual(a, b)           Verify that a == b
assertNotEqual(a, b)        Verify that a != b
assertTrue(x)               Verify that x is True
assertFalse(x)              Verify that x is False
assertIn(item, list)        Verify that item is in list
assertNotIn(item, list)     Verify that item is not in list
"""
