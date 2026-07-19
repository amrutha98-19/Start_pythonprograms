# ------------------------------------------ #
#  5. Create a New File using x Mode
# ------------------------------------------ # 
# "x" mode is used to create a new file. 
#  If the file already exists, Python raises an error.

# syntax:file = open("filename.txt", "x")
try:
    file = open("newsample.txt", "x")
    print("File created successfully")
    file.close()
except FileExistsError:
    print("File already exists")