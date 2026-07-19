# A lambda function is a small anonymous function written in a single line.
# syntax : lambda arguments: expression

sub=lambda a,b:a-b # Lambda function for subtraction
result=sub(20,10)  # Call the lambda function
print("substraction =",result) # Print the result
print("\n Another example")
print("*" * 20)

square=lambda num:num*num  # Lambda function for square
square_result=square(5) # Call the lambda function
print("square =",square_result)  # Print the result