#ValueError
# ValueError occurs when the user enters an invalid value
try:
    a=int(input("Enter  first number :")) # Get two numbers from the user
    b=int(input("Enter second  number:"))
    Result=a/b     # Perform division operation
    print("Result=",Result)    # Display the result
# Handle division by zero error
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Please enter valid numbers")