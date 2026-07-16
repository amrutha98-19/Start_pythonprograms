# Encapsulation -> Hiding data from direct access.

class Bank:
      # Constructor
    def __init__(self,balance):
        self.balance=balance  # Private variable

    # Method to display balance
    def display_balance(self):
        print("Balance:",self.balance)

b=Bank(20000) # Creating object
b.display_balance() # Accessing data through method

