# Add a single item to a set -> add()
# Add multiple items to a set -> update()

# Add a single item to a set
myset={5,6,7,8,9}  
print("Original Set:", myset)

print("\n Add")
print("*" * 20)


myset.add(10)
print("After add:",myset)

# Add multiple items to a set

print("\n Update")
print("*" * 20)

myset.update([11,14,15])
print("After update:",myset)