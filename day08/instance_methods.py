class person:
    
    # Constructor

    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job


    
    # Instance Method
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Job:",self.job)

# Creating object
person1 = person("Anupama", 30, "Marketting manager")

# Calling instance method
person1.display()

