# Identity operators are used to check whether two variables refer to the same object in memory.
# is -> True if both variables point to same object
# is not ->True if both variables point to different object

a=[4,5,6]
b=[4,5,6]
c=a
print(a is b)      # a is b → False because a and b are different list objects, even though they contain the same values.
print(a is c)      # a is b → False because a and b are different list objects, even though they contain the same values.