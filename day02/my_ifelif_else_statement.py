# The if...elif...else statement checks multiple conditions. If one condition is True, its block executes. If none of the conditions are True, the else block executes.
marks=int(input("Enter your mark:"))
if marks>=90:
    print(f" Your mark is {marks} : Grade A ")
elif(marks>=70):
    print(f" Your mark is {marks} : Grade B ")
elif(marks>=55):
    print(f" Your mark is {marks} : Grade C ")
else:
    print(f" Your mark is {marks} : Failed ")


