# python mini project: Student Grade calculator


print("Student Grade Calculator")
print("*" * 25)

# Input student details
name = input("Enter student name: ")
subjects = int(input("Enter number of subjects: "))

maximum_mark = float(input("Enter maximum mark for each subject: "))
total = subjects * maximum_mark
obtainedmarks = 0
# Collect marks with validation
for i in range(subjects):
    while True:
        marks = float(input(f" Enter marks for subject {i+1}: "))

        if 0 <= marks <= maximum_mark:
            obtainedmarks += marks
            break
        else:
            print(f"Invalid input! Marks must be between 0 and {maximum_mark}.")
# Calculate percentage
percentage = (obtainedmarks / total) * 100

# Assign grade

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "Fail"

# Display results
print("\n Student Result")
print("*" * 25)
print("Name         :", name)
print("Total Marks  :", obtainedmarks)
print("Percentage   :", round(percentage, 2), "%")
print("Grade        :", grade)
