f = open("YY_File Handling/Sample.txt", "r")
data = f.read()

"""
print(data)       # Will print the whole File Content
print(type(data))

"""
# Reading a set number of characters :-
f.seek(0) # Moves the cursor for reading writing file for the specific char(0)-> Start of the file 
chars = f.read(20) 
print(chars)   # Will Print the First 20 letts of the file


f.seek(0)
# Reading the file line by line
line1 = f.readline()
line2 = f.readline()
print(line1)
print(line2)

# Closing a file
f.close()


# Using the With Statement 
"""
with open("YY_File Handling/Sample.txt") as f:
  print(f.read())

-> Then you do not have to worry about closing your files, the with statement takes care of that.

"""

# Using loop to print the lines 

"""
with open("YY_File Handling/Sample.txt") as f:
  for x in f:
    print(x)
"""