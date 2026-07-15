# Odd number
#  An odd number is a number that leaves a remainder of 1 when divided by 2.

n=int(input("Enter number:"))
if n%2!=0:
    print(f"{n} is an odd number")
else:
    print(f"{n} is not an odd number")