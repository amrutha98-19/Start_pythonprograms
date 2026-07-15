
# Prime Number Program
# Prime number has only 2 factors: 1 and itself.
# Examples: 2, 3, 5, 7, 11
# Numbers <= 1 are not prime.


num = int(input("Enter number: "))

if num > 1:
    # Check factors from 2 to num-1
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")

