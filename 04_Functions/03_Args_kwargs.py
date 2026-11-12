# args* and kwargs** in Python Functions
"""
args* and kwargs** are used to pass a variable number of arguments to a function.
args* is used to pass a variable number of positional arguments.
kwargs** is used to pass a variable number of keyword arguments.
"""

# A function can accept any number of positional arguments with *args.
# Inside the function, args is a tuple.

def add_numbers(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(add_numbers(2, 4))
print(add_numbers(1, 2, 3, 4, 5))

# A function can accept any number of keyword arguments with **kwargs.
# Inside the function, kwargs is a dictionary.

def show_profile(**profile):
    for key, value in profile.items():
        print(f"{key}: {value}")

show_profile(name="John", age=30, country="USA")
show_profile(name="Alice", age=25, country="Canada", profession="Engineer")

# Using *args with Regular Arguments
# Regular arguments must be listed before *args in the function definition.

def greet(greeting, *names):
    for name in names:
        print(f"{greeting}, {name}!")

greet("Hello", "Alice", "Bob", "Charlie")


# Using **kwargs with Regular Arguments
# Regular arguments must be listed before **kwargs in the function definition.

def display_info(title, **info):
    print(f"Title: {title}")
    for key, value in info.items():
        print(f"{key}: {value}")

display_info("Employee Details", name="John", age=30, department="HR")

# Combining *args and **kwargs in a Function
# You can use both *args and **kwargs in the same function.

def show_details(*args, **kwargs):
    print("Positional Arguments:")
    for arg in args:
        print(arg)
    
    print("\nKeyword Arguments:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_details(1, 2, 3, name="Alice", age=25, country="Canada") 

# Output:
# Positional Arguments:
# 1
# 2
# 3

# Keyword Arguments:
# name: Alice
# age: 25
# country: Canada

# Unpacking Arguments with * and **
# You can unpack a list or tuple into positional arguments using *.

def multiply(a, b, c):
    return a * b * c

numbers = [2, 3, 4]
print(multiply(*numbers))  # Output: 24

# You can also unpack a dictionary into keyword arguments using **.

def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

person = {"name": "Alice", "age": 25, "country": "Canada"}
print_info(**person)  # Output:
# name: Alice
# age: 25
# country: Canada

