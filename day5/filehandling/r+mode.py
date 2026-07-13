# r+ mode -> Read and Write
# ------------------------------------------ # 
# 6. Read and Write using r+ Mode
#  ------------------------------------------ #
#  "r+" mode is used for both reading and writing.
#  The file must already exist.


file = open("sample.txt", "r+")

# Read the file content
content = file.read()
print("File Content:")
print(content)
file.write("\nSimple and powerful language.")

file.close()