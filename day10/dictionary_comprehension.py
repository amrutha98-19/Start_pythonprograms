# ------------------------------------------
# Normal Way
# ------------------------------------------

print("Normal way")
print("*" * 20)

# Create an empty dictionary
numbers = {}

# Loop through numbers from 1 to 7
for i in range(1, 8):
    # Store the number as the key and its square as the value
    numbers[i] = i * i

# Display the dictionary
print(numbers)


# ------------------------------------------
# Dictionary Comprehension
# ------------------------------------------

print("\nDictionary comprehension")
print("*" * 20)

# Create a dictionary in a single line
# Key   -> i
# Value -> i * i
numbers = {i: i * i for i in range(1, 8)}

# Display the dictionary
print( numbers)