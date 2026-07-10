
person={"name":"Arun",
        "age":26,
        "city":"Kollam"
        }
print("Create dictionary:",person) # Print the complete dictionary

print("\n Add iems from dictionary") # Display section heading
print("*" * 20)
# Add a new key-value pair
person["job"] = "Python Developer"
print(person)



print("\n Update iems from dictionary") # Display section heading
print("*" * 20)


person["city"]="palakkad"
person["age"]=30
print(person)