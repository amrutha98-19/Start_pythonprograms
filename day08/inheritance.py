# Inheritance -> One class can inherit properties and methods from another class.



# Parent class (Base class)
class Animal:
    def sound(self):
        print("Animals make sounds")


# Child class (Derived class)
class cat(Animal):
      # Child class method
    def meow(self):
        print("Cat meows")

# Creating an object of the Cat class
c = cat()


c.sound() # Calling parent class method using child object
c.meow() # Calling child class method