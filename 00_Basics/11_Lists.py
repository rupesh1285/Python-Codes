# Create a List:

created_list = ["apple", "banana", "cherry"]
print(created_list)

# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.

# List with duplicate values:
duplicate_values_list = ["apple", "banana", "cherry", "apple", "cherry"]
print(duplicate_values_list)

# List Length
print(len(duplicate_values_list))

# List Items - Data Types
# List items can be of any data type:

string_items_list = ["apple", "banana", "cherry"]
integer_items_list = [1, 5, 7, 9, 3]
boolean_items_list = [True, False, False]

# A list can contain different data types:
mixed_data_types_list = ["abc", 34, True, 40, "male"]

# type()
print(type(mixed_data_types_list))
print(type(integer_items_list))
print(type(boolean_items_list))
print(type(mixed_data_types_list[0]))
print(type(mixed_data_types_list[1]))
print(type(mixed_data_types_list[2]))
print(type(mixed_data_types_list[3]))
print(type(mixed_data_types_list[4]))

# The list() Constructor
constructed_list = list(("apple", "banana", "cherry")) # note the double round brackets
print(constructed_list)

# Negative Indexing
negative_indexing_list = ["apple", "banana", "cherry"]
print(negative_indexing_list[-1]) # Returns the last item
print(negative_indexing_list[-2]) # Returns the second last item

# Range of Indexes
range_indexing_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(range_indexing_list[2:5]) # Returns items from index 2 to 4 (5 is not included)
print(range_indexing_list[:4]) # Returns items from the beginning to index 3 (4 is not included)
print(range_indexing_list[2:]) # Returns items from index 2 to the end
print(range_indexing_list[-4:-1]) # Returns items from index -4 to -2 (the item at index -1 is not included)

# Check if Item Exists
membership_check_list = ["apple", "banana", "cherry"]
if "apple" in membership_check_list:
  print("Yes, 'apple' is in the fruits list")

# Change Item Value
changed_value_list = ["apple", "banana", "cherry"]
changed_value_list[1] = "blackcurrant"
print(changed_value_list)

# Change a Range of Item Values
range_changed_value_list = ["apple", "banana", "cherry", "orange", "
kiwi", "mango"]
range_changed_value_list[1:3] = ["blackcurrant", "watermelon"]
print(range_changed_value_list)

# Insert Items
inserted_items_list = ["apple", "banana", "cherry"]
inserted_items_list.insert(2, "watermelon") # Inserts "watermelon" at index 2
print(inserted_items_list)

# Append Items
appended_items_list = ["apple", "banana", "cherry"]
appended_items_list.append("orange") # Appends "orange" to the end of the list
print(appended_items_list)

# Extend List
extended_list = ["apple", "banana", "cherry"]
tropical = ["pineapple", "papaya", "mango"]
extended_list.extend(tropical) # Extends the list by adding all items from the tropical list
print(extended_list)

# Add Any Iterable
iterable_list = ["apple", "banana", "cherry"]
tuple_items = ("kiwi", "orange")
iterable_list.extend(tuple_items) # Extends the list by adding all items from the tuple
print(iterable_list)

# Remove Specified Item
removed_item_list = ["apple", "banana", "cherry"]
removed_item_list.remove("banana") # Removes "banana" from the list
print(removed_item_list)

# Remove Item at Specified Index
removed_index_list = ["apple", "banana", "cherry"]
del removed_index_list[1] # Removes the item at index 1
print(removed_index_list)

# Del Keyword
del_keyword_list = ["apple", "banana", "cherry"]
del del_keyword_list # Deletes the entire list
print(del_keyword_list) # This will cause an error because the list is deleted

# pop() Method
pop_method_list = ["apple", "banana", "cherry"]
popped_item = pop_method_list.pop() # Removes and returns the last item
print(popped_item) # Prints the popped item

# Clear List
clear_list = ["apple", "banana", "cherry"]
clear_list.clear() # Clears all items from the list
print(clear_list) # Prints an empty list

# Loop Through a List
loop_list = ["apple", "banana", "cherry"]
for fruit in loop_list:
  print(fruit)

# Loop Through a List Using Indexes
index_loop_list = ["apple", "banana", "cherry"]
for i in range(len(index_loop_list)):
  print(index_loop_list[i])


# Loop Through a List Using While Loop
while_loop_list = ["apple", "banana", "cherry"]
i = 0
while i < len(while_loop_list):
  print(while_loop_list[i])
  i += 1

# List Comprehension
comprehension_list = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in comprehension_list if "a" in x] # Returns a new list containing only the items with the letter "a"
print(newlist)


# Sorting Lists
# Sort List Alphanumerically
sort_list = ["banana", "Orange", "Kiwi", "cherry"]
sort_list.sort()
print(sort_list)

numeric_sort_list = [100, 50, 65, 82, 23]
numeric_sort_list.sort()
print(numeric_sort_list)

# Sort List Reverse Alphanumerically
reverse_sort_list = ["banana", "Orange", "Kiwi", "cherry"]
reverse_sort_list.sort(reverse=True)
print(reverse_sort_list)

reverse_numeric_sort_list = [100, 50, 65, 82, 23]
reverse_numeric_sort_list.sort(reverse=True)
print(reverse_numeric_sort_list)




