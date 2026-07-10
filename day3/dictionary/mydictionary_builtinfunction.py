person={"name":"Arun",
        "age":26,
        "city":"Kollam",
        "job":"python devolper",
        }
print("Create dictionary:",person) # Print the complete dictionary

print("\n Builtin functions ") # Display section heading
print("*" * 20)
# len() -> Returns the number of key-value pairs
print("Length:", len(person))
# type() -> Returns the data type of the object
print("Type:", type(person))
# str() -> Converts dictionary to string
print("String:", str(person))

# dict() -> Creates a new dictionary
new_dict = dict(person)
print("New Dictionary:", new_dict)

# sorted() -> Returns a sorted list of keys
print("Sorted Keys:", sorted(person))


# max() -> Returns the largest key alphabetically
print("Maximum Key:", max(person))

# min() -> Returns the smallest key alphabetically
print("Minimum Key:", min(person))


# any() -> Returns True if at least one key is True
print("Any:", any(person))

# all() -> Returns True if all keys are True
print("All:", all(person))