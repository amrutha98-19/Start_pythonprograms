

# ------------------------------------------ 
# 4. Append Data to a File
# ------------------------------------------ #
#  "a" mode is used to add new data to a file.
#   Old data will not be removed.
# syntax:file = open("filename.txt", "a")
file=open('sample.txt','a')
file.write("\n Python is easy to learn")
file.close()
print("Data append successfully")