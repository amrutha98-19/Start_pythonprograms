# ------------------------------------------ 
#  2. Read from a File #
#  ------------------------------------------ 
#  "r" mode is used to read data from a file.
#  Syntax:  file = open("filename.txt", "r")

file=open('sample.txt','r')
content=file.read()
print(content)
file.close()
