# Large Codebases have many functions, and it can be difficult to keep track of what types of arguments a function expects and what type it returns. 
# Type hints are a way to provide this information in the code itself, making it easier to understand and use functions correctly.

# Example of a function with type hints
def greet(name: str) -> str:
    return f"Hello, {name}!"

# Example of a function with type hints for multiple arguments
def add_numbers(a: int, b: int) -> int:
    return a + b

# How it Works:
"""
1. The function greet takes a single argument name of type str and returns a value of type str.
2. The function add_numbers takes two arguments a and b, both of type int, and returns a value of type int.
3. If you try to call these functions with arguments of the wrong type, you will get a TypeError at runtime.
"""