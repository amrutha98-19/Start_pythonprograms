# ------------------------------------------
#  # 3. Write to a File
# ------------------------------------------ # 
# "w" mode is used to write data to a file. 
#  If the file does not exist, Python creates it. 
# If the file already exists, old content is removed.
#  Syntax:  file = open("filename.txt", "w")

file=open('sample.txt','w')
file.write("Python is highlevel programming language \n")
file.write("Interpreted language")
file.close()
print("Data write successfully")