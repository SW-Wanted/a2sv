# Data types
"""
Built-in Python data types by category:

Category           | Types
-------------------|-----------------------------------------------
Text Type          | str
Numeric Types      | int, float, complex
Sequence Types     | list, tuple, range
Mapping Type       | dict
Set Types          | set, frozenset
Boolean Type       | bool
Binary Types       | bytes, bytearray, memoryview
None Type          | NoneType
"""

# Getting the type
x = 5
print(type(x))

"""
Example                           | Data Type
----------------------------------|-----------
x = "Hello World"                 | str
x = 20                            | int
x = 20.5                          | float
x = 1j                            | complex
x = ["apple", "banana", "cherry"] | list
x = ("apple", "banana", "cherry") | tuple
x = range(6)                      | range
x = {"name": "John", "age": 36}   | dict
x = {"apple", "banana", "cherry"} | set
x = frozenset({"apple","banana"}) | frozenset
x = True                          | bool
x = b"Hello"                      | bytes
x = bytearray(5)                  | bytearray
x = memoryview(bytes(5))          | memoryview
x = None                          | NoneType
"""

# Setting the Specific Data Type
# If you want to specify the data type, you can use the following constructor functions:
"""
Example                                      | Data Type   |
---------------------------------------------|-------------|
x = str("Hello World")                       | str         |
x = int(20)                                  | int         |
x = float(20.5)                              | float       |
x = complex(1j)                              | complex     |
x = list(("apple", "banana", "cherry"))      | list        |
x = tuple(("apple", "banana", "cherry"))     | tuple       |
x = range(6)                                 | range       |
x = dict(name="John", age=36)                | dict        |
x = set(("apple", "banana", "cherry"))       | set         |
x = frozenset(("apple", "banana", "cherry")) | frozenset   |
x = bool(5)                                  | bool        |
x = bytes(5)                                 | bytes       |
x = bytearray(5)                             | bytearray   |
x = memoryview(bytes(5))                     | memoryview  |
"""

x = range(6)
print(x)

# Python Numbers
# There are three numeric types in Python:
"""
- int
- float
- complex
"""

x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))

# Int
# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

print('Integer Examples:')
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

# Float
# Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

print('Float Examples:')
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

# Float can also be scientific numbers with an "e" to indicate the power of 10.
print('Scientific Float Examples:')
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

# Complex
# Complex numbers are written with a "j" as the imaginary part:

print('Complex Examples:')

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

# Type Conversion
# You can convert from one type to another with the int(), float(), and complex() methods:

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# Random Number
# Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:

# Example
# Import the random module, and display a random number from 1 to 9:
import random

print(random.randrange(1, 10))

# Python Casting
# Casting in python is therefore done using constructor functions:

# - int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
# - float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
# - str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals

# Example
print('Integers:')
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
print(f'x: {x} : {type(x)}'); print(f'y: {y} : {type(y)}'); print(f'z: {z} : {type(z)}');

print('Floats:')
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
print(f'x: {x} : {type(x)}'); print(f'y: {y} : {type(y)}'); print(f'z: {z} : {type(z)}'); print(f'w: {w} : {type(w)}');

print('Strings:')
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
print(f'x: {x} : {type(x)}'); print(f'y: {y} : {type(y)}'); print(f'z: {z} : {type(z)}');

