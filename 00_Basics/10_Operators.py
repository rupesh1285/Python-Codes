# Addition (+)

sum1 = 100 + 50      # 150 (100 + 50)
sum2 = sum1 + 250    # 400 (150 + 250)
sum3 = sum2 + sum2   # 800 (400 + 400)
print(sum1)
print(sum2)
print(sum3)

# Arithmetic Operators

x = 5
y = 3

print(x + y)  # Addition
print(x - y)  # Subtraction
print(x * y)  # Multiplication
print(x / y)  # Division
print(x % y)  # Modulus
print(x ** y)  # Exponentiation
print(x // y)  # Floor Division

# Assignment Operators

x1 = 5
x1 += 3  # x1 = x1 + 3 -> 8
x1 -= 3  # x1 = x1 - 3 -> 5 
x1 *= 3  # x1 = x1 * 3 -> 15
x1 /= 3  # x1 = x1 / 3 -> 5
x1 %= 3  # x1 = x1 % 3 -> 2
x1 **= 3  # x1 = x1 ** 3 -> 8
x1 //= 3  # x1 = x1 // 3 -> 2
x1 := 3  # x1 = 3     (Walrus Operator)
x1 <<= 3  # x1 = x1 << 3 -> 24
x1 >>= 3  # x1 = x1 >> 3 -> 3
x1 &= 3  # x1 = x1 & 3 -> 3
x1 |= 3  # x1 = x1 | 3 -> 3
x1 ^= 3  # x1 = x1 ^ 3 -> 0

# Ternary Operator (Conditional Expression)
# Syntax: value_if_true if condition else value_if_false

age = 20
status = "adult" if age >= 18 else "minor"
print(status)  # Output: adult  

# Instead of Elif: The ternary operator can be used instead of elif in longer if statements
num = 6

x = "Fri" if num == 5 else "Sat" if num == 6 else "Sun" if num == 7 else "weekday"

print(x)

# Comparison Operators
a = 10
b = 20

print(a == b)  # Equal
print(a != b)  # Not equal
print(a > b)   # Greater than
print(a < b)   # Less than
print(a >= b)  # Greater than or equal
print(a <= b)  # Less than or equal

# Chained Comparison Operators
c = 5
d = 10
e = 15

print(c < d < e)  # True (5 < 10 and 10 < 15)
print(c > d > e)  # False (5 > 10 and 10 > 15)

# Logical Operators
m = True
n = False   

print(m and n)  # False (True AND False)
print(m or n)   # True (True OR False)  
print(not m)    # False (NOT True)

# Identity Operators :- (is, is not)

x2 = ["apple", "banana"]
y2 = ["apple", "banana"]
z2 = x2

print(x2 is z2) # True (x2 and z2 refer to the same object in memory)
print(x2 == z2) # True (x2 and z2 have the same content)
print(x2 is y2) # False (x2 and y2 refer to different objects in memory)

print(x2 is not z2) # False (x2 and z2 refer to the same object in memory)
print(x2 != z2) # False (x2 and z2 have the same content
print(x2 is not y2) # True (x2 and y2 refer to different objects in memory)

# Membership Operators :- (in, not in)

fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)  # True (banana is in the list)
print("grape" not in fruits)  # True (grape is not in the list)
print("apple" in fruits)  # True (apple is in the list)

# Bitwise Operators
x3 = 5  # Binary: 0101
y3 = 3  # Binary: 0011

print(x3 & y3)  # Bitwise AND: 0101 & 0011 = 0001 (1)
print(x3 | y3)  # Bitwise OR: 0101 | 0011 = 0111 (7)
print(x3 ^ y3)  # Bitwise XOR: 0101 ^ 0011 = 0110 (6)
print(~x3)      # Bitwise NOT: ~0101 = 1010 (-6)
print(x3 << 1)  # Bitwise Left Shift: 0101 << 1 = 1010 (10)
print(x3 >> 1)  # Bitwise Right Shift: 0101 >> 1 = 0010 (2)


# Operator Precedence
# Operator precedence determines the order in which operations are performed in an expression. Operators with higher precedence

# 1. Parentheses ()
# 2. Exponentiation **
# 3. Unary operators +, -, ~
# 4. Multiplication *, /, //, %
# 5. Addition +, -
# 6. Bitwise shift <<, >>
# 7. Bitwise AND &
# 8. Bitwise XOR ^
# 9. Bitwise OR |
# 10. Comparison operators ==, !=, <, >, <=, >=
# 11. Logical operators and, or, not

# Left-to-Right Evaluation
# In the absence of parentheses, operators are evaluated from left to right.
# For example, in the expression 2 + 3 * 4, the multiplication is performed first (due to higher precedence), resulting in 2 + 12 = 14.
# If we want to change the order of operations, we can use parentheses: (2 + 3) * 4 = 5 * 4 = 20.











