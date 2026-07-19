# Logical Operators-Logical operators are used to combine two or more conditions.
#and -> Returns True if both conditions are True
#or -> Returns True if at least one condition is True
#not -> Reverse the result

age = 20

print(age >= 18 and age <= 60) #and → Check if the age is between 18 and 60.
print(age < 18 or age > 60) # or → Check if the age is below 18 or above 60.
print(not(age < 18)) #not → Reverse the condition.