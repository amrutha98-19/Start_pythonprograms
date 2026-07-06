# A nested if statement is an if statement inside another if statement.
num1=int(input("Enter your number:"))
if num1>0:
    if num1%2==0:
        print("positive even")
    else:
        print("positive odd")
else:
    print("negative number")