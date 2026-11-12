"""Examples of variable scope and name resolution in Python.

Scope is the region of a program where a name can be accessed. Python
resolves names using the LEGB rule:

    Local -> Enclosing -> Global -> Built-in

The examples in this file are intentionally executable. Run the file to see
the output from each scope demonstration.
"""


# ---------------------------------------------------------------------------
# 1. Global scope
# ---------------------------------------------------------------------------

# A name defined at the top level of a module belongs to global scope.
app_name = "Scope Demo"


def show_global_name():
    # A function can read a global name when there is no local name with the
    # same spelling.
    print("Global name:", app_name)


show_global_name()


# ---------------------------------------------------------------------------
# 2. Local scope
# ---------------------------------------------------------------------------

def show_local_name():
    # This variable exists only while this function is running.
    message = "This is a local variable."
    print(message)


show_local_name()

# The following would raise NameError because message is local to the
# function. It is shown as a comment so the lesson itself remains runnable.
# print(message)


# Every function call gets its own local scope. Local variables from separate
# calls do not overwrite one another.
def create_greeting(name):
    greeting = f"Hello, {name}!"
    return greeting


print(create_greeting("Asha"))
print(create_greeting("Ravi"))


# ---------------------------------------------------------------------------
# 3. The LEGB lookup rule
# ---------------------------------------------------------------------------

legb_name = "global value"


def demonstrate_legb():
    legb_name = "local value"

    def nested_function():
        # Python finds legb_name in the enclosing function before looking in
        # the module's global scope.
        return legb_name

    return nested_function()


print("LEGB lookup:", demonstrate_legb())


# ---------------------------------------------------------------------------
# 4. Enclosing scope and closures
# ---------------------------------------------------------------------------

def make_multiplier(factor):
    # factor is local to make_multiplier, but enclosing for multiply.
    def multiply(number):
        return number * factor

    return multiply


double = make_multiplier(2)
triple = make_multiplier(3)
print("Closure:", double(5))
print("Closure:", triple(5))


# A closure remembers values from its enclosing scope even after the
# enclosing function has returned.
def make_counter():
    count = 0

    def get_next_count():
        nonlocal count
        count += 1
        return count

    return get_next_count


counter = make_counter()
print("Counter:", counter())
print("Counter:", counter())


# ---------------------------------------------------------------------------
# 5. The nonlocal keyword
# ---------------------------------------------------------------------------

# Without nonlocal, assigning to setting inside update_setting would create a
# new local variable instead of changing the enclosing variable.
def make_setting():
    setting = "development"

    def update_setting(new_setting):
        nonlocal setting
        setting = new_setting
        return setting

    return update_setting


change_setting = make_setting()
print("Before/after enclosed update:", change_setting("production"))


# ---------------------------------------------------------------------------
# 6. The global keyword
# ---------------------------------------------------------------------------

visit_count = 0


def record_visit():
    global visit_count
    visit_count += 1
    return visit_count


print("Visits:", record_visit())
print("Visits:", record_visit())


# Reading a global value does not require the global keyword. The keyword is
# needed only when assigning to the global name inside a function.
def reset_visits():
    global visit_count
    visit_count = 0


reset_visits()
print("Visits after reset:", visit_count)


# Prefer returning a new value or using an object when possible. Global state
# can make code harder to test and can create unexpected dependencies.
def increment(value):
    return value + 1


current_value = 10
current_value = increment(current_value)
print("Value without global state:", current_value)


# ---------------------------------------------------------------------------
# 7. Variable shadowing
# ---------------------------------------------------------------------------

status = "global status"


def show_shadowing():
    # This local status shadows the global status only inside this function.
    status = "local status"
    print("Inside function:", status)


show_shadowing()
print("Outside function:", status)


# A parameter is also a local variable and can shadow a global name.
language = "Python"


def show_language(language):
    print("Parameter:", language)


show_language("JavaScript")
print("Global language:", language)


# ---------------------------------------------------------------------------
# 8. Block scope: if, for, and while do not create a new scope
# ---------------------------------------------------------------------------

if True:
    block_value = "created inside an if block"


print("No block scope:", block_value)

for loop_value in range(1):
    pass


print("Loop variable still exists:", loop_value)


# Functions do create a new scope, unlike if and for blocks.
def create_function_scope():
    function_value = "inside a function"
    return function_value


print(create_function_scope())
# print(function_value)  # NameError: function_value is local to the function.


# ---------------------------------------------------------------------------
# 9. Comprehension scope
# ---------------------------------------------------------------------------

# The iteration variable in a comprehension has its own scope in Python 3.
number = "global number"
numbers = [number for number in range(3)]
print("Comprehension result:", numbers)
print("Name after comprehension:", number)


# The comprehension can use names from the surrounding scope.
multiplier = 10
scaled_numbers = [value * multiplier for value in range(3)]
print("Comprehension using outer name:", scaled_numbers)


# ---------------------------------------------------------------------------
# 10. Exception-handler scope
# ---------------------------------------------------------------------------

try:
    10 / 0
except ZeroDivisionError as error:
    # error is available inside the except block.
    print("Handled exception:", type(error).__name__)


# Python clears the exception target after the except block to release the
# traceback reference. This name should not be used outside the block.
# print(error)  # NameError


# ---------------------------------------------------------------------------
# 11. Built-in scope
# ---------------------------------------------------------------------------

# Built-in names such as len, sum, and print are found last in LEGB.
items = ["Python", "Java", "Go"]
print("Built-in len:", len(items))
print("Built-in sum:", sum([1, 2, 3]))


# Avoid naming variables after built-in functions. If a built-in is shadowed,
# it can no longer be called normally in that scope.
def demonstrate_builtin_shadowing():
    len = "not the built-in len"
    return len


print("Shadowed built-in:", demonstrate_builtin_shadowing())


# ---------------------------------------------------------------------------
# 12. Class scope
# ---------------------------------------------------------------------------

class User:
    # This name belongs to the class namespace.
    category = "standard"

    def __init__(self, name):
        # self.name belongs to this particular object instance.
        self.name = name

    def describe(self):
        # Instance attributes are accessed through self.
        return f"{self.name} ({self.category})"


user = User("Kiran")
print("Class and instance scope:", user.describe())


# A method does not automatically close over class-local names by bare name.
# Use the class name or self to access a class attribute.
class Configuration:
    mode = "safe"

    def get_mode(self):
        return Configuration.mode


print("Class attribute:", Configuration().get_mode())


# ---------------------------------------------------------------------------
# 13. Default arguments and scope
# ---------------------------------------------------------------------------

# Default argument expressions are evaluated once, when the function is
# defined, not each time it is called.
default_label = "initial"


def show_default_label(label=default_label):
    return label


default_label = "changed"
print("Captured default:", show_default_label())
print("Explicit argument:", show_default_label(default_label))


# Use None when a function needs a fresh mutable value for every call.
def collect_value(value, collected=None):
    if collected is None:
        collected = []
    collected.append(value)
    return collected


print("Fresh list:", collect_value("A"))
print("Fresh list:", collect_value("B"))


# ---------------------------------------------------------------------------
# 14. Module entry-point scope
# ---------------------------------------------------------------------------

def main():
    """Run the small entry-point demonstration."""
    print("main() ran in module:", __name__)


# When this file is run directly, __name__ is "__main__". When imported,
# this block does not run automatically.
if __name__ == "__main__":
    main()
