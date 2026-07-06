# smallest of three numbers
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))
if(num1<=num2 and num1<=num3):
    print(f"The first number {num1} is smallest number")
elif(num2<=num1 and num2<=num3):
    print(f"The second number {num2} is smallest number")
else:
    print(f"The third number {num3} is smallest number")