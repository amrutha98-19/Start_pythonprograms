# Product of First n Natural Numbers (Factorial)
#syntax:factorial *= i

num=int(input("Enter number:"))
factorial=1
for i in range(1,num+1):
    factorial*=i
print("factorial=",factorial)