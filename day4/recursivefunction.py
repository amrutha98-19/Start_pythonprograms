# Recursive function ->  A function that calls itself to solve smaller subproblems of the same problem
def factorial(num):
    # Base case
    if num==0 or num==1:
        return 1
    # Recursive call
    return num*factorial(num-1)
# Function calls
print(factorial(5))
print(factorial(0))