# Convert a Python object containing all the legal data types:

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# print(json.dumps(x)) # will print Json String, which will be hard to read 

"""
# Using the indent parameter to define the numbers of indents:
print(json.dumps(x, indent=4))
"""

"""
# Using Seperators:
print(json.dumps(x, indent=4, separators=(". ", " = ")))
"""

"""
# Order the result
"""
print(json.dumps(x, indent=4, sort_keys=True)
)

