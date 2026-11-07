# Error : Using double quotes inside a string that is also enclosed in double quotes will cause a syntax error. To fix this, you can either use single quotes to enclose the string or escape the inner double quotes with a backslash.

txt = "We are the so-called "Vikings" from the north."

# Corrected version: Using Escape Characters(\"")
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

# Other escape characters include:
# \' - Single Quote
txt2 = 'It\'s a beautiful day!'
print(txt2)

# \\ - Backslash
txt3 = "This is a backslash: \\"
print(txt3)

# \n - New Line
txt4 = "Hello\nWorld!"
print(txt4)

# \t - Tab
txt5 = "Hello\tWorld!"
print(txt5)

# \b - Backspace
txt6 = "Hello\bWorld!"
print(txt6)

# \r - Carriage Return
txt7 = "Hello\rWorld!"
print(txt7)

# \f - Form Feed
txt8 = "Hello\fWorld!"
print(txt8)

# \v - Vertical Tab
txt9 = "Hello\vWorld!"
print(txt9)

# \ooo - Octal value
txt10 = "This is an octal value: \101"
print(txt10)

# \xhh - Hex value
txt11 = "This is a hex value: \x41"
print(txt11)

