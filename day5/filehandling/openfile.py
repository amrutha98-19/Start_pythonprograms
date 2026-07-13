# ========================================== 
# # Python File Handling Examples # 
# ==========================================

# ------------------------------------------ 
# # 1. Open a File 
# # ------------------------------------------ #
#  open() is used to open a file.
#  Syntax: # file = open("filename.txt", "mode")

file=open('sample.txt','r')
print("file opened successfully")
file.close()
