# The match statement is used to perform different actions based on different conditions.

day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")


"""
Default Value
Use the underscore character _ as the last case value if you want a code block to execute when there are not other matches:
"""
day = 4
match day:
  case 6:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _:
    print("Looking forward to the Weekend")

# Combining Cases
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("It's a weekday")
  case 6 | 7:
    print("It's a weekend")

# If-statements as Guards
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if day < 5:
    print("It's a weekday")
  case 6 | 7:
    print("It's a weekend")

