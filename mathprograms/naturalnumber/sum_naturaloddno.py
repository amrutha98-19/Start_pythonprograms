# Find the sum of odd numbers up to n
#syntax: sum_odd += i where i % 2 != 0
num=int(input("Enter number:"))
sum_odd=0
for i in range(1,num+1):
    if i%2!=0:
        sum_odd+=i
print("sum of odd numbers=",sum_odd)