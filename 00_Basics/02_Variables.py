# Integer
x = 5
print(x)

# String
student = "John"
print(student)

"""
Rules For Naming Variables in Python

1. A variable name must start with a letter or the underscore character
2. Python is Case-Sensitive(age, Age and AGE are three different variables)
3. A variable name cannot start with a number
4. A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
5. A variable name cannot be any of the Python keywords.

"""

# Global Variables

x = "awesome"

def myfunc():
    print(x)

myfunc()

# The global variable x is still "awesome"

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

## Global Keyword

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

# Global Keword to Change Global Variable

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

