#  Basic Try Except Example

# The try block contains code that may cause an exception (error).
# The except block handles the exception if an error occurs in the try block.
try:
    a=int(input("Enter  first number:"))  # Get two numbers from the user
    b=int(input("Enter second  number:"))
    Result=a/b     # Perform division operation
    print("Result=",Result)    # Display the result
except:
    print("An error occured")     # Execute if an error occurs