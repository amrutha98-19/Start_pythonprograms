# ------------------------------------------
# Normal Way
# ------------------------------------------

print("Normal way")
print("*" * 20)

# Create an empty list
squares = []

# Loop from 1 to 7
for i in range(1, 8):
    # Square each number and add it to the list
    squares.append(i * i)

# Display the list of squares
print("Squares:", squares)


# ------------------------------------------
# List Comprehension
# ------------------------------------------

print("\nList comprehension")
print("*" * 20)

# Create the list of squares in a single line
squares = [i * i for i in range(1, 8)]

# Display the list of squares
print("Squares:", squares)