# Count vowels and consonants
m=input("Enter String:")
vowels="aeiouAEIOU"
vowel_count=0
consonant_count=0
for ch in m:
    if ch.isalpha():
        if ch in vowels:
            vowel_count+=1
        else:
            consonant_count+=1
print("Vowels=",vowel_count)
print("Consonants=",consonant_count)
