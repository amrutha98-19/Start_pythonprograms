# Find the common elements in two lists
list1=[1,2,3,4,5,6]
list2=[7,8,9,2,10,11]
for i in list1:
    for j in list2:
        if i==j:
            print("The common element  is :",j)