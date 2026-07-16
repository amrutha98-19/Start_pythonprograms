# class -> A class is a blueprint or template for creating objects.
# object -> An object is an instance of a class.

# Creating a class named Person

class person:
    name="Anna"
    age=26
    job="python devolper"

# Creating an object (instance) of the Person class
person1=person()

# Accessing and printing class variables using the object
print("Name:",person1.name)
print("Age:",person1.age)
print("Job:",person1.job)