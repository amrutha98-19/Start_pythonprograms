# Print prime numbers in a range

print("Prime numbers")
print("*" * 20)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

for num in range(a, b + 1):
    if num > 1:              # Prime numbers are > 1
        for i in range(2, num):  # Check factors
            if num % i == 0:
                break
        else:                # No factors found
            print(num)