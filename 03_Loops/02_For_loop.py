# For Loops In Python

# For loops are used to iterate over a sequence (like a list, tuple, dictionary, set, or string) and execute a block of code for each item in the sequence.

# Normal for Loop 
for i in range(5):
    print(i)

# For loop with a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Break and Continue Statements

for i in range(5):
    if i == 3:
        break  # Exit the loop when i is 3
    print(i)

for i in range(5):
    if i == 3:
        continue  # Skip the rest of the loop when i is 3
    print(i)

# the else Statement in For Loops
for i in range(5):
    print(i)
else:
    print("Loop is finished")

# The Range Function
for i in range(5):
    print(i)

# Nested Loops
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")

# The Pass Statement
for i in range(5):
    pass  # Do nothing, just a placeholder

# 
