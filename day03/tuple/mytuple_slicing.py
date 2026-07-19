# Slicing -> Extracts a portion of the tuple using indexes.
# Remember: in slicing, the start index is included and the end index is exclude

 # Syntax: tuple[start:end]

numbers=(20,30,40,50,60)
print("Slice1:",numbers[1:4]) # Index 1 to 3(4 excluded)
print("Slice2:",numbers[:3])  # Beginning to index 2
print("Slice3:",numbers[3:]) # Index 3 to the end
print("Slice4:",numbers[-3:])   # Last 3 elements
print("Slice5:",numbers[::-1])  # Reverse tuple