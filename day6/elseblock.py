# Day 6 - Else Block Example
# The else block executes only if no exception occurs in the try block
try:
    # Get two numbers from the user
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    # Perform division operation
    result = a / b

# Handle division by zero error
except ZeroDivisionError:
    print("Cannot divide by zero")

# Handle invalid input error
except ValueError:
    print("Please enter valid numbers")

# Execute if no exception occurs
else:
    print("Result =", result)
    print("Program executed successfully")