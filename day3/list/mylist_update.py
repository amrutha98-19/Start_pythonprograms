# update
mylist=[5,6,7,8,9] 

print("orginal list:",mylist)

# Positive Index Update ->Beginning of the list
mylist[0]=4  #Replaces the first element 5 with 4.
mylist[1:3]=[2,3] #Replaces elements at index 1 and 2 (6 and 7) with 2 and 3
print("Update:",mylist)

# Negative Index Update -> End of the list

mylist[-1]=10
print("Negative update:",mylist)
