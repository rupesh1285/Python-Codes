"""Examples of parameters and arguments in Python functions."""


# A parameter is the variable listed in a function definition.
# An argument is the value passed to the function when it is called.
def greet(name):
    print(f"Hello, {name}!")


greet("Emil")  # "Emil" is the argument for the name parameter.


# Default parameter values are used when no argument is supplied.
def introduce(country="Norway"):
    print(f"I am from {country}.")


introduce("Sweden")
introduce("India")
introduce()  # Uses the default value: Norway.


# Positional arguments are matched with parameters by their order.
def print_children(child1, child2, child3):
    print(f"The youngest child is {child3}.")


print_children("Emil", "Tobias", "Linus")


# Keyword arguments are matched by parameter name, so their order does not
# matter. Using keyword arguments also makes a function call easier to read.
print_children(child1="Emil", child2="Tobias", child3="Linus")


# Positional and keyword arguments can be mixed. Positional arguments must
# come before keyword arguments.
print_children("Emil", child2="Tobias", child3="Linus")


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


show_profile(name="Asha", role="Developer", country="India")


# Lists, tuples, dictionaries, and other objects can be passed as arguments.
def print_fruits(fruits):
    for fruit in fruits:
        print(fruit)


fruit_list = ["Apple", "Banana", "Mango"]
print_fruits(fruit_list)


# A parameter can be made positional-only by placing / in the definition.
# The parameter name cannot be used as a keyword argument.
def calculate_area(length, width, /):
    return length * width


print(calculate_area(5, 3))


# A parameter can be made keyword-only by placing * in the definition.
# The argument must be supplied using its parameter name.
def create_user(name, *, active=True):
    status = "active" if active else "inactive"
    return f"{name} ({status})"


print(create_user("Ravi"))
print(create_user("Ravi", active=False))


# Parameters can have type hints and a return type. Type hints document the
# expected values; Python does not enforce them automatically at runtime.
def multiply(first: int, second: int) -> int:
    return first * second


print(multiply(6, 7))


# Required parameters must receive a value every time the function is called.
# Parameters with defaults are optional and can be omitted.
def make_full_name(first_name, last_name="Unknown"):
    return f"{first_name} {last_name}"


print(make_full_name("Neha", "Sharma"))
print(make_full_name("Neha"))


# A default value can be combined with *args. The default parameter comes
# before *args, and any extra positional values are collected in a tuple.
def show_scores(student, passing_score=40, *scores):
    passed_scores = [score for score in scores if score >= passing_score]
    return f"{student}: {passed_scores}"


print(show_scores("Asha", 50, 45, 70, 32, 90))
print(show_scores("Asha", 40, 35, 55))


# A required keyword-only parameter has no default value. It must be supplied
# by name because it appears after the * marker.
def send_message(message, *, recipient):
    return f"To {recipient}: {message}"


print(send_message("Meeting at 10", recipient="Ravi"))


# The / and * markers can be used together. This gives complete control over
# which parameters can be positional and which must be keyword arguments.
def register_device(device_id, /, model, *, operating_system):
    return f"{device_id}: {model} running {operating_system}"


print(register_device("DEV-101", "Laptop", operating_system="Linux"))
print(register_device("DEV-102", model="Phone", operating_system="Android"))


# The special * marker by itself makes every parameter after it keyword-only.
def format_address(*, street, city, country="India"):
    return f"{street}, {city}, {country}"


print(format_address(street="MG Road", city="Pune"))


# A list or tuple can be unpacked into positional arguments with *.
coordinates = (12.97, 77.59)
print("Coordinates:", coordinates)


def show_coordinates(latitude, longitude):
    return f"Latitude: {latitude}, Longitude: {longitude}"


print(show_coordinates(*coordinates))


# A dictionary can be unpacked into keyword arguments with **. Its keys must
# match the parameter names in the function definition.
user_details = {"name": "Kiran", "role": "Tester"}


def describe_user(name, role):
    return f"{name} works as a {role}."


print(describe_user(**user_details))


# A function can combine positional-only parameters, normal parameters,
# *args, keyword-only parameters, and **kwargs in one signature.
def configure(
    name,
    /,
    category="general",
    *tags,
    enabled=True,
    **options,
):
    return {
        "name": name,
        "category": category,
        "tags": tags,
        "enabled": enabled,
        "options": options,
    }


print(
    configure(
        "search",
        "feature",
        "python",
        "functions",
        enabled=True,
        timeout=30,
    )
)


# None is commonly used as the default for an optional value. This avoids
# using a mutable list as a default value, which would be shared by calls.
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items


print(add_item("Book"))
print(add_item("Pen"))


# A caller can pass a custom list when shared results are intentional.
shopping_list = ["Milk"]
print(add_item("Bread", shopping_list))
