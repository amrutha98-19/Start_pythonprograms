# Sum of odd Whole Numbers

# Syntax:
# if i % 2 != 0:
#     sum_odd += i
num=int(input("Enter number:"))
sum_odd=0
for i in range(1,num+1):
    if i%2!=0:
        sum_odd+=i
print("sum of odd numbers=",sum_odd)