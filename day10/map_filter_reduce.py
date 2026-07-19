# map()    -> Applies a function to all items in an iterable.
# filter() -> Filters items based on a condition.
# reduce() -> Reduces all items to a single value.



from functools import reduce

# List of numbers
n = [5, 6, 7, 8, 9]

# Square each number using map()
squared = list(map(lambda i: i * i, n))

# Filter even numbers using filter()
even = list(filter(lambda i: i % 2 == 0, n))

# Find the sum of all numbers using reduce()
total = reduce(lambda i, j: i + j, n)

print("Squared:", squared)
print("Even:", even)
print("Total:", total)