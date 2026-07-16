# Instance Variable -> Variables that belong to an object.

class person:

  
    def __init__(self,name,age,job):
        # Instance Variables
        self.name=name    
        self.age=age       
        self.job=job       


# Creating object
person1=person("Anna",26,"python devolper")

# Accessing instance variables
print("Name:",person1.name)
print("Age:",person1.age)
print("Job:",person1.job)
        

