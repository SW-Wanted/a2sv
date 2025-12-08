# Python Strings
# Strings in python are surrounded by either single quotation marks, or double quotation marks.
# 'hello' is the same as "hello".

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

# Multi-Line Strings
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# String are Arrays
# Like many other popular programming languages, strings in Python are arrays of unicode characters.

a = "Hello, World!"
print(a[1])

# Looping Through a String
for x in "banana":
  print(x)

# String Length
a = "Hello, World!"
print(len(a))

# Check String
txt = "The best things in life are free!"
print("free" in txt); print("expensive" not in txt);
if "free" in txt:
  print("Yes, 'free' is present.")
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

# Slicing String
# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.

# Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5])

# Slice To the End - Get the characters from the start to position 5 (not included):
b = "Hello, World!"
print(b[:5])

# Slice From the Start - Get the characters from position 2, and all the way to the end:

b = "Hello, World!"
print(b[2:])

# Negative Indexing
# Use negative indexes to start the slice from the end of the string:
# Get the characters from position -5 to position -2 (not included):
b = "Hello, World!"
print(b[-5:-2])

# Python - Modify Strings

# Upper Case
a = "Hello, World!"
print(a.upper())

# Lower Case
a = "Hello, World!"
print(a.lower())

# Remove Whitespace
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

# Replace String
a = "Hello, World!"
print(a.replace("H", "J"))

# Split String
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

# Python - String Concatenation
# To concatenate, or combine, two strings you can use the + operator.
a = "Hello"
b = "World"
c = a + " " + b
print(c)

# Python - Strings Format
# As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:
# age = 36
# txt = "My name is John, I am " + age # This will raise an error.

# But we can combine strings and numbers by using the format()
age = 36
txt = f"My name is John, I am {age}"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

price = 59000
txt = f"The price is {price:,} dollars"
print(txt)

price = 49
txt = "The price is {} dollars"
print(txt.format(price))

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

txt = f"The price is {20 * 59} dollars"
print(txt)

"""
Formatting Types

| Code | Description |
|------|-------------|
| `:<` | Left aligns the result (within the available space) |
| `:>` | Right aligns the result (within the available space) |
| `:^` | Center aligns the result (within the available space) |
| `:=` | Places the sign to the left-most position |
| `:+` | Use a plus sign to indicate if the result is positive or negative |
| `:-` | Use a minus sign for negative values only |
| `: ` | Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers) |
| `:,` | Use a comma as a thousand separator |
| `:_` | Use an underscore as a thousand separator |
| `:b` | Binary format |
| `:c` | Converts the value into the corresponding Unicode character |
| `:d` | Decimal format |
| `:e` | Scientific format, with a lower case e |
| `:E` | Scientific format, with an upper case E |
| `:f` | Fixed point number format |
| `:F` | Fixed point number format, in uppercase (show inf and nan as INF and NAN) |
| `:g` | General format |
| `:G` | General format (using an upper case E for scientific notations) |
| `:o` | Octal format |
| `:x` | Hex format, lower case |
| `:X` | Hex format, upper case |
| `:n` | Number format (locale-aware) |
| `:%` | Percentage format |
"""

# Python - Escape Characters
# To insert characters that are illegal in a string, use an escape character.
# An escape character is a backslash \ followed by the character you want to insert.

txt = "We are the so-called \"Vikings\" from the north."

# Escape Characters
# Other escape characters used in Python:


# Code    | Result
# --------|----------------
# \'      | Single Quote    
# \\      | Backslash       
# \n      | New Line        
# \r      | Carriage Return  
# \t      | Tab             
# \b      | Backspace       
# \f      | Form Feed       
# \ooo    | Octal value     
# \xhh    | Hex value       
