# Python Conditions and If statements

"""
Python supports the usual logical conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
These conditions can be used in several ways, most commonly in "if statements" and loops.

An "if statement" is written by using the if keyword.
"""

# If statement
a = 33
b = 200
if b > a:
    print("b is greater than a")  # Output: b is greater than a

# Multiple statements
age = 20
if age >= 18:
  print("You are an adult")
  print("You can vote")
  print("You have full legal rights")


# Elif statement
age = 15
if age < 13:
    print("You are a child")
elif age < 20:
    print("You are a teenager")  # Output: You are a teenager
else:
    print("You are an adult")
    print("You have full legal rights")
