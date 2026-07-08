# Built-in Functions
# len()  -> Returns the number of items in the list.
# max()  -> Returns the largest item in the list.
# min()  -> Returns the smallest item in the list.
# sum()  -> Returns the sum of all numeric items in the list.
# list(seq) -> Converts a sequence into a list.

list1 = [1, 2, 3, 4, 5, 6, 7, 8]

print("Built-in Functions")
print("*" * 30)

# len()
print("Length of list:", len(list1))

# max()
print("Maximum element in list:", max(list1))

# min()
print("Minimum element in list:", min(list1))

# sum()
print("Sum of list elements:", sum(list1))


print("\nConvert String to List")
print("*" * 30)

# list(seq) - String to List
text = "java"
print("Original string:", text)
print("Converted list:", list(text))


print("\nConvert Tuple to List")
print("*" * 30)

# list(seq) - Tuple to List
data = (20, 30, 40, 50, 60)
print("Original tuple:", data)
print("Converted list:", list(data))