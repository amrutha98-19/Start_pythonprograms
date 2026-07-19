# Check palindrome or not
text=input("Enter text:").lower()
is_palindrome=True
length=len(text)
for i in range(length//2):
    if text[i]!=text[length-1-i]:
        is_palindrome=False
        break
if is_palindrome:
    print(f"The text {text} is a palindrome")
else:
    print(f"The text {text} is not a palindrome")