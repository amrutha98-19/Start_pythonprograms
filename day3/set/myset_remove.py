# Removing items from a set
myset={4,5,6,7,8,9,10,10}  
print("Original Set:", myset)

print("\n Remove")
print("*" * 20)


# remove() -> Removes the specified item

myset.remove(8)
print("After remove(8):", myset)

print("\n Discard")
print("*" * 20)

# discard() -> Removes the item if it exists
myset.discard(4)
print("After discard(4):", myset)


print("\n Pop")
print("*" * 20)


# pop() -> Removes and returns a random item
removeditem = myset.pop()
print("Removed Item using pop():", removeditem)
print("After pop():", myset)


print("\n Clear")
print("*" * 20)
# clear() -> Removes all items from the set
myset.clear()
print("After clear():", myset)
