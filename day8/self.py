# self refers to the current object.
class person:
    def __init__(self,name):
        self.name=name
    def display(self):
        print("Name:", self.name)
person1=person("Annmery")
person1.display()