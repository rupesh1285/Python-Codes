# When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
# These exceptions can be handled using the try statement:


# The try block will generate an exception, because x is not defined:
try:
  print(x)
except:
  print("An exception occurred")

## Multiple Exceptions:
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

# Else Statement: the else keyword to define a block of code to be executed if no errors were raised.
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

# Finally: The finally block, if specified, will be executed regardless if the try block raises an error or not.
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")


#### Raise Keyword: We can choose to throw an exception if a condition occurs.
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")


# Another Example:
x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")

