# creating a Set 

mySet = {1, 2, 3, 4, 5}
print(mySet)

# Set Properties
# - Unordered
# - Unchangeable
# - Duplicates Not Allowed

# Duplicates will be removed automatically
mySet1 = {1, 2, 3, 4, 5, 1, 2, 3}
print(mySet1)  # Output: {1, 2, 3, 4, 5}

# Sets are Unordered- Means that the items do not have a defined order, and cannot be referred to by index or key.
#print(mySet1[0])  # This will raise an error because sets are unordered.

# Sets can carry different data types
mySet2 = {1, "Hello", 3.14, True}
# True is considered as 1 in Python, so it will be treated as a duplicate and removed.
print(mySet2)  # Output: {1, 'Hello', 3.14}
# Similarly, False is considered as 0 in Python, so it will be treated as a duplicate and removed.


# Length of a Set
print(len(mySet2))  # Output: 3

# Type of a Set
print(type(mySet2))  # Output: <class 'set'>

# Creating a Set using the set() constructor
mySet3 = set((1, 2, 3, 4, 5))
print(mySet3)  # Output: {1, 2, 3, 4, 5}

# Accessing Set Items
# Sets are unordered, so we cannot access items using indexing or slicing.
for item in mySet3:
    print(item)  # Output: 1, 2, 3, 4, 5 (in any order)

# Checking if an item exists or not in a Set
print(3 in mySet3)  # Output: True
print(6 in mySet3)  # Output: False 
print(6 not in mySet3)  # Output: True

# Adding Items to a Set
# Adding a single item using the add() method
mySet3.add(6)
print(mySet3)  # Output: {1, 2, 3, 4, 5, 6}

# Adding multiple items to a Set
# Adding multiple items using the update() method
mySet3.update([7, 8, 9])
print(mySet3)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9}

# Adding items from another set
mySet4 = {10, 11, 12}
mySet3.update(mySet4)
print(mySet3)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

# Removing Items from a Set
# Removing an item using the remove() method
mySet3.remove(12)
print(mySet3)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}

# Removing an item using the discard() method
mySet3.discard(11)
print(mySet3)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# Removing an item using the pop() method
# The pop() method removes a random item from the set.
popped_item = mySet3.pop()
print(popped_item)  # Output: Random item from the set
print(mySet3)  # Output: Set after removing the random item

# Clearing a Set
mySet3.clear()
print(mySet3)  # Output: set() (an empty set)

# Deleting a Set
del mySet3
# print(mySet3)  # This will raise an error because the set has been deleted.

# Looping through a Set
mySet5 = {1, 2, 3, 4, 5}
for item in mySet5:
    print(item)  # Output: 1, 2, 3, 4, 5 (in any order)

# Joining Sets
# Using the union() method

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1.union(set2)
print(set3)  # Output: {1, 2, 3, 4, 5}

# Using the update() method
set1.update(set2)
print(set1)  # Output: {1, 2, 3, 4, 5}

# Using (the | operator)
set4 = {1, 2, 3}
set5 = {3, 4, 5}
set6 = set4 | set5
print(set6)  # Output: {1, 2, 3, 4, 5}

# Joining Multiple Sets
set7 = {1, 2, 3}
set8 = {"a", "b", "c"}
set9 = {7, 8, 9}
set10 = set7.union(set8, set9)
print(set10)  # Output: {1, 2, 3, 'a', 'b', 'c', 7, 8, 9}

# Intersection of Sets
# Using the intersection() method
set11 = {1, 2, 3, 4, 5}
set12 = {4, 5, 6, 7, 8}
set13 = set11.intersection(set12)
print(set13)  # Output: {4, 5}

# Using the & operator
set14 = {1, 2, 3, 4, 5}
set15 = {4, 5, 6, 7, 8}
set16 = set14 & set15
print(set16)  # Output: {4, 5}

# Intersection Update
set17 = {1, 2, 3, 4, 5}
set18 = {4, 5, 6, 7, 8}
set17.intersection_update(set18)
print(set17)  # Output: {4, 5}

# Using the &= operator
set19 = {1, 2, 3, 4, 5}
set20 = {4, 5, 6, 7, 8}
set19 &= set20
print(set19)  # Output: {4, 5}

# Difference of Sets
# Using the difference() method
set21 = {1, 2, 3, 4, 5}
set22 = {4, 5, 6, 7, 8}
set23 = set21.difference(set22)
print(set23)  # Output: {1, 2, 3}

# Using the - operator
set24 = {1, 2, 3, 4, 5}
set25 = {4, 5, 6, 7, 8}
set26 = set24 - set25
print(set26)  # Output: {1, 2, 3}

# Difference Update
set27 = {1, 2, 3, 4, 5}
set28 = {4, 5, 6, 7, 8}
set27.difference_update(set28)
print(set27)  # Output: {1, 2, 3}

# Using the -= operator
set29 = {1, 2, 3, 4, 5}
set30 = {4, 5, 6, 7, 8}
set29 -= set30
print(set29)  # Output: {1, 2, 3}

# Symmetric Difference of Sets
# Using the symmetric_difference() method
set31 = {1, 2, 3, 4, 5}
set32 = {4, 5, 6, 7, 8}
set33 = set31.symmetric_difference(set32)
print(set33)  # Output: {1, 2, 3, 6, 7, 8}

# Using the ^ operator
set34 = {1, 2, 3, 4, 5}
set35 = {4, 5, 6, 7, 8}
set36 = set34 ^ set35
print(set36)  # Output: {1, 2, 3, 6, 7, 8}

# Symmetric Difference Update
set37 = {1, 2, 3, 4, 5}
set38 = {4, 5, 6, 7, 8}
set37.symmetric_difference_update(set38)
print(set37)  # Output: {1, 2, 3, 6, 7, 8}

# Frozensets
# Frozensets are immutable sets, meaning that the items of a frozenset cannot be changed after creation.
# Creating a frozenset

myFrozenset = frozenset([1, 2, 3, 4, 5])
print(myFrozenset)  # Output: frozenset({1, 2, 3, 4, 5})

# Frozensets Methods
# Frozensets support methods like union(), intersection(), difference(), and symmetric_difference() just like regular sets.
set39 = {1, 2, 3}
frozenset1 = frozenset([3, 4, 5])
# Union of a set and a frozenset
set40 = set39.union(frozenset1)
print(set40)  # Output: {1, 2, 3, 4, 5}

# Intersection of a set and a frozenset
set41 = {1, 2, 3}
frozenset2 = frozenset([3, 4, 5])
set42 = set41.intersection(frozenset2)
print(set42)  # Output: {3}

# Difference of a set and a frozenset
set43 = {1, 2, 3}
frozenset3 = frozenset([3, 4, 5])
set44 = set43.difference(frozenset3)
print(set44)  # Output: {1, 2}

# Symmetric Difference of a set and a frozenset
set45 = {1, 2, 3}
frozenset4 = frozenset([3, 4, 5])
set46 = set45.symmetric_difference(frozenset4)
print(set46)  # Output: {1, 2, 4, 5}

