# Day 6 - Multiple Exceptions Example
# Multiple Exception Handling is the process of handling more than one type of exception in a program.

try:
    # Create a list
    flowers = ["Rose", "Jasmin", "Lotus", "Hibiscus"]

    # Get index from the user
    index = int(input("Enter index number: "))

    # Display fruit name
    print("Flowers:", flowers[index])

# Handle invalid input
except ValueError:
    print("Please enter a valid number")

# Handle invalid index
except IndexError:
    print("Index out of range")