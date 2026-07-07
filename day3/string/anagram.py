text1=input("Enter first text:")
text2=input("Enter second text:")
text1=text1.lower().replace(" ", "")
text2=text2.lower().replace(" ", "")
if len(text1)!=len(text2):
    print("The second text is not anagram of the first")
else:
    sorted_text1=sorted(text1)
    sorted_text2=sorted(text2)
    if sorted_text1==sorted_text2:
        print("second text is an anagram of the first")
    else:
        print("second text is not an anagram of the first")
        