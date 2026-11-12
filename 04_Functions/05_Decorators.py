# Basic Decorator 
"""
A decorator is a function that takes another function as an argument and extends the behavior of the latter function without explicitly modifying it.
"""

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

print(myfunction())


