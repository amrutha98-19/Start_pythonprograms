# Method Overriding -> Child class changes the parent class method.
# Parent class (Base class)
class Animal:
    # Parent class method
    def sound(self):
        print("Animals make sounds")

# Child class
class Cat(Animal):
    # Overriding the parent method
    def sound(self):
        print("Cat meows")
# Creating object of child class
c = Cat()

# Calling overridden method
c.sound()