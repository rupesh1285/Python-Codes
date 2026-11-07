# String Methods

s = "Hello, World!"
print(s.capitalize())  # Capitalizes the first letter of the string
print(s.upper())  # Converts the string to uppercase
print(s.lower())  # Converts the string to lowercase
print(s.title())  # Capitalizes the first letter of each word in the string
print(s.casefold())  # Converts the string to lowercase (more aggressive than lower())
print(s.center(20, "*"))  # Centers the string and fills with a specified character
print(s.count("o"))  # Counts the occurrences of a substring in the string
print(s.endswith("!"))  # Checks if the string ends with a specified substring
print(s.startswith("Hello"))  # Checks if the string starts with a specified substring
print(s.find("World"))  # Returns the index of the first occurrence of a substring
print(s.index("World"))  # Returns the index of the first occurrence of a substring (raises an error if not found)
print(s.isalnum())  # Checks if all characters in the string are alphanumeric
print(s.isalpha())  # Checks if all characters in the string are alphabetic
print(s.isdigit())  # Checks if all characters in the string are digits
print(s.islower())  # Checks if all characters in the string are lowercase
print(s.isupper())  # Checks if all characters in the string are uppercase
print(s.isspace())  # Checks if all characters in the string are whitespace
print(s.join(["Hello", "World"]))  # Joins a list of strings with the


