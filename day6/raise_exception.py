# raise exception
# raise is used to create and throw an exception manually in Python
try:
    age=int(input("Enter your age:"))
      # Raise exception if age is less than 18
    if(age<18):
        raise ValueError
    else:
        print("The age is valid")
except ValueError:
     print("The age is  not valid")
