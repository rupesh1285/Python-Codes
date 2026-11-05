# Strings
print("Hello")
print('Hello')

# quotes inside a string
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

# Assigning a String to a Variable
a = "Hello"
print(a)

# Multiline Strings
b = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(b)

c = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(c)

# Strings are Arrays
d = "Hello, World!"
print(d[1])

# Looping Through a String
for x in "banana":
  print(x)  

# String Length
e = "Hello, World!"
print(len(e))

# Check String
f = "The best things in life are free!"
print("free" in f)

# Check if NOT in String
g = "The best things in life are free!"
print("expensive" not in g)

# Using if Statement
h = "The best things in life are free!"
if "free" in h:
  print("Yes, 'free' is present.")  

if "expensive" not in g:
  print("Yes, 'expensive' is NOT present.")