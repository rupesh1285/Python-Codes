try:
    number = int(input("Enter a number: "))
    print("Result:", 10 / number)
except ValueError:
    print("Please enter a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("The calculation completed successfully.")
finally:
    print("Program finished.")
