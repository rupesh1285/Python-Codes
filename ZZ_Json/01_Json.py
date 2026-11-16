import json

# Conversion from JSON to Python

# JSON data is represented as text before loading.
# x = '''{
#     "name": "John",
#     "age": 30,
#     "city": "New York"
# }'''

# y = json.loads(x)

# print(y)

# Conversion from Python to JSON

x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Convert the Python dictionary into a JSON string.
y = json.dumps(x)

# The result is a JSON string.
print(y)


# Python objects that can be converted into JSON strings:
# - dict
# - list
# - tuple
# - string
# - int
# - float
# - True
# - False
# - None

# When converting from Python to JSON, these equivalent types are used:
#
# Python    JSON
# dict      Object
# list      Array
# tuple     Array
# str       String
# int       Number
# float     Number
# True      true
# False     false
# None      null