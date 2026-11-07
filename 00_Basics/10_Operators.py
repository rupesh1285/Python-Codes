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







