#count consonants
#A consonant is an alphabet that is not a vowel (a, e, i, o, u).

mystring=input("Enter your text:")
count=0
for ch in mystring:
    if ch.isalpha() and ch not in 'aeiou':  # isalpha()->isalpha() returns True if the string contains only letters. Otherwise, it returns False.s
        count+=1
print("Count consonants:",count)


#Count vowels
mystring=input("Enter your sentence:")


