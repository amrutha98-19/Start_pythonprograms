# FileNotFoundError
# FileNotFoundError occurs when Python tries to open a file that does not exist.
try:
    file=open("demo.txt","r")
    content=file.read()
    print(content)

except FileNotFoundError:
    print("File not found")
finally:
    print("This block always executes")