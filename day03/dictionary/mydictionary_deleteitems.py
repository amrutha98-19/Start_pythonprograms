
person={"name":"Arun",
        "age":26,
        "city":"Kollam",
        "job":"python devolper",
        }
print("Create dictionary:",person) # Print the complete dictionary

print("\n Remove iems from dictionary") # Display section heading
print("*" * 20)

# Remove item using del keyword
del person["city"]
print("After deleting city:", person)

# Remove item using pop()
person.pop("age")
print("After removing age:", person)

#  Remove last inserted item using popitem()
person.popitem()
print("After popitem():", person)

# Remove all items using clear()
person.clear()
print("After clear():", person)