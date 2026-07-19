person={"name":"Arun",
        "age":26,
        "city":"Kollam",
        "job":"python devolper",
        }
print("Create dictionary:",person) # Print the complete dictionary

print("\nDictionary Methods")
print("*" * 20)

# keys() -> Returns all keys in the dictionary
print("Keys:", person.keys())
# values() -> Returns all values in the dictionary
print("Values:", person.values())
# items() -> Returns all key-value pairs as tuples
print("Items:", person.items())

# get() -> Returns the value of the specified key
print("Job:", person.get("job"))


# setdefault() -> Returns the value of the key.
# If the key does not exist, it adds the key with the given value.
person.setdefault("country", "India")
print("After setdefault():", person)

# copy() -> Creates a copy of the dictionary
new_person = person.copy()
print("Copied Dictionary:", new_person)

# pop() -> Removes the specified key and returns its value
removed_value = person.pop("age")
print("Removed Value:", removed_value)
print("After pop():", person)

# popitem() -> Removes the last inserted key-value pair
person.popitem()
print("After popitem():", person)

# clear() -> Removes all items from the dictionary
person.clear()
print("After clear():", person)

