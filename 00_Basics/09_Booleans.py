print(10 > 9)
print(10 == 9)
print(10 < 9)

# The bool() function
print(bool("Hello"))
print(bool(15))

# Most Values are True

# Any string is True, except empty strings.
print(bool("abc"))
print(bool(""))

# Any number is True, except 0.
print(bool(123))
print(bool(3.14))
print(bool(0))

# Any list, tuple, set, and dictionary are True, except empty ones.
print(bool(["apple", "cherry", "banana"]))
print(bool([]))
print(bool(("apple", "cherry", "banana")))
print(bool(()))

# Some Values are False
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
print(bool(set()))
print(bool(range(0)))

# The __len__ method can be used to control the boolean value of an object.
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))