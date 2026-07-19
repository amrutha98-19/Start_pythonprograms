# Set methods
myset = {10, 20, 30,40}
myset.add(50)
print("After add():",myset)
myset.update([60, 70])
print("After update():", myset)

myset.remove(20)
print("After remove():", myset)

myset.discard(70)
print("After discard():", myset)

copiedset = myset.copy()
print("Copied Set:", copiedset)