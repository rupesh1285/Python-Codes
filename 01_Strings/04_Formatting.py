# Creating a string using f-string formatting

age = 36
txt = f"My name is John, I am {age}"
print(txt)

# Creating a string using .format() method

quantity = 3
itemno = 567    
price = 49.95
myorder = "I want {} pieces of item {} for ${:.2f}"
print(myorder.format(quantity, itemno, price))

# Creating a string using .format() method with positional arguments

quantity1 = 3
itemno1 = 567    
price1 = 49.95
myorder1 = "I want {0} pieces of item {1} for ${2:.2f}"
print(myorder1.format(quantity1, itemno1, price1))


# Creating a string using .format() method with keyword arguments

quantity2 = 3
itemno2 = 567    
price2 = 49.95
myorder2 = "I want {quantity} pieces of item
    {itemno} for ${price:.2f}"
print(myorder2.format(quantity=quantity2, itemno=itemno2, price=price2))

# Creating a string using f-string formatting with expressions 
txt = f"The price is {20 * 59} dollars"
print(txt)