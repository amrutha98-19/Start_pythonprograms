# Check whether the given string is palindrome or not

m=input("Enter String:")
m=m.lower()
if m==m[::-1]:
    print(f"{m} is a palidrome")
else:
    print(f"{m} is not a palidrome")