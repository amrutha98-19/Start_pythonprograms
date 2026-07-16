# polymorphism -> The same method name can work differently for different objects.

class cat:
    def sound(self):    # sound() method for Cat
        print("Meow")
class lion:
    def sound(self):    # sound() method for Lion
        print("Roar")

# Creating objects
cat=cat()
lion=lion()

# Calling the same method for different objects
cat.sound()
lion.sound()