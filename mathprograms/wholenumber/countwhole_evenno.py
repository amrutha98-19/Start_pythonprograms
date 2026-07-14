# Count Even Numbers from 0 to N
num=int(input("Enter number:"))
count=0
for i in range(num+1):
    if i%2==0:
        print(i, end=" ")
        count+=1
    
print("\nnumber of evennumbers:",count)