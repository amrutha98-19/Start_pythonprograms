# Average of First N Whole Numbers

num=int(input("Enter number:"))

sum=num*(num+1)/2 # Calculate the sum of whole numbers from 0 to N   # Formula: Sum = N × (N + 1) / 2

average=sum/(num+1) # Calculate the average of whole numbers from 0 to N  # Number of whole numbers from 0 to N is (N + 1)
print("Average=",average)