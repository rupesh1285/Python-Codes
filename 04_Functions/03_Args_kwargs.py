# args* and kwargs** in Python Functions
"""
args* and kwargs* are used to pass a variable number of arguments to a function.
args* is used to pass a variable number of positional arguments.
kwargs* is used to pass a variable number of keyword arguments.
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

