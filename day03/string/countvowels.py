#Count vowels
mystring=input("Enter your sentence:")


count=0
for ch in mystring:
    char_lower=ch.lower()
    if char_lower in 'aeiou':
        count+=1

print("Number of vowels:",count)