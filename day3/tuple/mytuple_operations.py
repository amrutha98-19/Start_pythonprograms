# Tuple operations
tuple1 = (1, 2, 3,4,5 , 6, 7,8)
print("index:",tuple1[0]) #indexing
print("slicing:",tuple1[1:5])#slicing
print("concatenation:",tuple1+(9,10)) # Concatenation
print("repetation:",tuple1*2)#Repetation

# Membership
print("\nmembership")
print("*" * 30)

print(3 in tuple1)
print(13 not in tuple1)

print("\niteration")
print("*" * 30)

# Iteration
for item in tuple1:
    print(item)