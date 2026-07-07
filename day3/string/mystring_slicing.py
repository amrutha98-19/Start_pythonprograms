# slice -> Slicing is used to extract a part of a string.
# syntax:string[start : stop : step]
mystring="Python Programming"
print("Entire string:",mystring[:])
print("From index 0 to 3:",mystring[0:4])
print("From index 6 to the end:",mystring[6:])
print("From the beginning to index:",mystring[:6])
print("Every second character:",mystring[::2])
print("Reverse the string",mystring[::-1])
print("Last 5 characters:",mystring[-5:])
print("All except the last 5 characters:",mystring[:-5])
