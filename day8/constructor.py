

# Constructor (__init__ method) -> A special method that runs automatically
# when an object is created and initializes object data.
class person:

    
    # class constructor
    def __init__(self,name,age,job):
        self.name=name     # Initialize name
        self.age=age        # Initialize age
        self.job=job       # Initialize job
        


person1=person("Anna",26,"python devolper") # Creating an object and passing values to the constructor



# Accessing and printing object data
print("Name:",person1.name)
print("Age:",person1.age)
print("Job:",person1.job)