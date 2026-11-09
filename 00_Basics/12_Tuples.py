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
print(type(thistuple3))  # <class 'tuple'>

# NOT a tuple
thistuple4 = ("apple")
print(type(thistuple4))  # <class 'str'>

# Creating a empty tuple
thistuple5 = ()
print(thistuple5)  # ()
print(type(thistuple5))  # <class 'tuple'>

# The tuple() Constructor
thistuple6 = tuple(("apple", "banana", "cherry"))
print(thistuple6)  # ('apple', 'banana', 'cherry')

# Tuple Items - Data Types

"""
Tuple items can be of any data type:
- String
- Integer
- Float
- List
- Tuple
- Dictionary

A tuple can contain different data types:
example: a tuple with strings, integers and boolean values
"""

thistuple = ("apple", 1, 3.14, True)
print(thistuple)

### Access Tuple Items

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# Negative Indexing
newtuple = ("apple", "banana", "cherry")
print(newtuple[-1])

# Range of Indexes
newtuple1 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(newtuple1[2:5])  # from index 2 to 5 (not included)
print(newtuple1[:4])  # from the beginning to index 4 (not included)
print(newtuple1[2:])  # from index 2 to the end

# Range of Negative Indexes
print(newtuple1[-4:-1])  # from index -4 to -1 (not included)

# Check if Item Exists
newtuple2 = ("apple", "banana", "cherry")
if "apple" in newtuple2:
    print("Yes, 'apple' is in the fruits tuple")

# Updating Tuples
"""
You cannot change the items in a tuple, but you can convert the tuple into a list, change the list, and convert the list back into a tuple.
"""

# Convert the tuple into a list to be able to change it
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y[1] = "kiwi"
thistuple = tuple(y)

# Example:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)  # ("apple", "kiwi", "cherry")

# Add tuple to a tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)  # ("apple", "banana", "cherry", "orange")

# Deleting Tuples

thistuple = ("apple", "banana", "cherry")
del thistuple
# print(thistuple)  # This will raise an error because the tuple is deleted

# Unpacking Tuples 
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)



# Using Asterisk*
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

# Tropic Astrik 
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits

print(green) # Will print the first item in the tuple
print(tropic) # Will print the items in the middle of the tuple
print(red) # Will print the last item in the tuple


# Loop Through a Tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

# Loop Through the Index Numbers
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])

# Looping Using a While Loop
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1

# Join Two Tuples
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)  # ('a', 'b', 'c', 1, 2, 3)

# Multiply Tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)  # ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')

# Tuple Methods

# count() - Returns the number of times a specified value occurs in a tuple
thistuple = ("apple", "banana", "cherry", "apple")
x = thistuple.count("apple")
print(x)  # 2

# index() - Searches the tuple for a specified value and returns the position of where it was found
thistuple = ("apple", "banana", "cherry")
x = thistuple.index("cherry")
print(x)  # 2

