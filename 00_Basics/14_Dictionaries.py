"""
As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
Dictionaries are used to store data values in key:value pairs. A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
They are mutable, meaning you can change their content without changing their identity.
Dictionaries are defined using curly braces {}.
"""

# Creating a Dictionary
myDict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(myDict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}
print(type(myDict))  # Output: <class 'dict'>
print(len(myDict))  # Output: 3
print(myDict["name"])  # Output: John
print(myDict.get("age"))  # Output: 30
print(myDict.keys())  # Output: dict_keys(['name', 'age', 'city'])
print(myDict.values())  # Output: dict_values(['John', 30, 'New York'])
print(myDict.items())  # Output: dict_items([('name', 'John'), ('age', 30), ('city', 'New York')])

# Duplicates will be removed automatically
# In this case, the second "age" key will overwrite the first one.
myDict2 = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "age": 25
}
print(myDict2)  # Output: {'name': 'John', 'age': 25, 'city': 'New York'}

# Constructing a Dictionary using the dict() constructor
myDict3 = dict(name="John", age=30, city="New York")
print(myDict3)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}

# Checking if a key exists in a Dictionary
print("name" in myDict)  # Output: True
print("age" in myDict)   # Output: True
print("country" in myDict)  # Output: False

# Adding Items to a Dictionary
myDict["country"] = "USA"
print(myDict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York', 'country': 'USA'}

# Updating Items in a Dictionary
myDict["age"] = 31
print(myDict)  # Output: {'name': 'John', 'age': 31, 'city': 'New York', 'country': 'USA'}

# Removing Items from a Dictionary
# Using the pop() method
myDict.pop("city")
print(myDict)  # Output: {'name': 'John', 'age': 31, 'country': 'USA'}

# Using the del keyword
del myDict["country"]
print(myDict)  # Output: {'name': 'John', 'age': 31}

# Using the clear() method
myDict.clear()
print(myDict)  # Output: {}

# Looping through a Dictionary
myDict4 = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

for key in myDict4:
    print(key, myDict4[key])  # Output: name John, age 30, city New York

for value in myDict4.values():
    print(value)  # Output: John, 30, New York

for key, value in myDict4.items():
    print(key, value)  # Output: name John, age 30, city New York

# Copying a Dictionary
myDict5 = myDict4.copy()
print(myDict5)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}

# Nested Dictionaries
myDict6 = {
    "person1": {
        "name": "John",
        "age": 30
    },
    "person2": {
        "name": "Jane",
        "age": 25
    }
}

print(myDict6)  # Output: {'person1': {'name': 'John', 'age': 30}, 'person2': {'name': 'Jane', 'age': 25}}
print(myDict6["person1"]["name"])  # Output: John
print(myDict6["person2"]["age"])  # Output: 25


# Nested Dictionaries Example

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)  # Output: {'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}
print(myfamily["child2"]["name"])  # Output: Tobias
print(myfamily["child3"]["year"])  # Output: 2011

# Looping through a Nested Dictionary
for child, info in myfamily.items():
    print(child, info)  # Output: child1 {'name': 'Emil', 'year': 2004}, child2 {'name': 'Tobias', 'year': 2007}, child3 {'name': 'Linus', 'year': 2011}
    for key, value in info.items():
        print(key, value)  # Output: name Emil, year 2004, name Tobias, year 2007, name Linus, year 2011


       