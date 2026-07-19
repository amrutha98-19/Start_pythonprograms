# Day 6 - Finally Block Example
# The finally block always executes whether an exception occurs or not.

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

# Execute only when no exception occurs
else:
    # Display the result
    print("Result =", result)

# Execute always

finally:
    print("Program execution completed")
