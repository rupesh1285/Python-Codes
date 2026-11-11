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


