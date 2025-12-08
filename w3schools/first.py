def greet():
    print("Emanuel")
    if 5 > 2:
        print("five is greater than two")
    print("Hello"); print("How are you", end=" "); print('Goodbye')
    print(3); print(0.1 + 0.2)
    print("i am", 21, 'year old')

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
    print()

def f(n):
    if (n <= 2):
        return 1
    return f(n - 1) + f(n - 2)

x = 10
print(x)
fib(x)
print(f(x))

# Data Types
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# Check the data types
print(type(x))
print(type(y))

# Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# In the print() function, you output multiple variables, separated by a comma:
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
print(x + y + z)

x = 5
y = 10
print(x + y)

x = 5
y = "John"
print(x, y)

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)