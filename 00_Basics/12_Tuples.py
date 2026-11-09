# Creating a Tuple

thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Tuples can also be created without the parentheses:

thistuple1 = "apple", "banana", "cherry"
print(thistuple1)

# Notes 
"""
Tuple items are ordered, unchangeable, and allow duplicate values.
Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
"""

# Tuples allow duplicate values:
thistuple2 = ("apple", "banana", "cherry", "apple")
print(thistuple2)

# Tuple Length
print(len(thistuple2))

# Create a tuple with one item
thistuple3 = ("apple",)
