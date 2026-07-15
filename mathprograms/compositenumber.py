# composite number
# A composite number is a number that has more than two factors (1, itself, and other factors).

# Examples: 4, 6, 8, 9, 10, 12.

num = int(input("Enter number: "))

if num <= 1:                                         # Numbers less than or equal to 1 are not composite
    print(f"{num} is not a composite number.")
else:
    is_composite = False                               # Assume the number is not composite

    for i in range(2, num):                             # Check for factors from 2 to num-1
        if num % i == 0:                                 # If the number is divisible by i, it has another factor
            is_composite = True
            break                                         # Stop checking once a factor is found
            
    if is_composite:
        print(f"{num} is a composite number.")
    else:
        print(f"{num} is not a composite number.")