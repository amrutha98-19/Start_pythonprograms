# Abstraction -> Showing important details and hiding implementation details.

from abc import ABC,abstractmethod

class Animal(ABC): # Abstract class

    # Abstract method
    @abstractmethod
    def sound(self):
        pass
class cat(Animal):
        # Implementing abstract method
      def sound(self):
        print("Cat meows")
# Creating object
c = cat()

# Calling method
c.sound()


