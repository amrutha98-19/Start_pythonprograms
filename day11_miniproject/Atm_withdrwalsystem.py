# A small Withdrawal System using Python Console + OOP concepts


class Bank_account():

    def __init__(self, name, account_number, balance):
        self.Name = name
        self.Accountnumber = account_number
        self.Balance = balance

    # Check Balance
    def checkbalance(self):
        print("Current Balance:", self.Balance)

    # Deposit
    def deposit(self, amount):
        if amount > 0:
            self.Balance += amount
            print(amount, "is deposited successfully.")
        else:
            print("Invalid amount")

    # Withdraw
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")

        elif amount > self.Balance:
            print("Insufficient Balance")

        else:
            self.Balance -= amount
            print(amount, "is Withdrawn successfully")

    # Account Details
    def accountdetails(self):
        print("\n--- Account Details ---")
        print("Name:", self.Name)
        print("Account Number:", self.Accountnumber)
        print("Balance:", self.Balance)


# User Input
account_number = input("Enter Account Number: ")
name = input("Enter Name: ")
balance = float(input("Enter Initial Balance: "))


# Create Object
account = Bank_account(name, account_number, balance)


# Menu
while True:

    print("\n===== BANK WITHDRAWAL SYSTEM =====")
    print("1. Account Details")
    print("2. Check Balance")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        account.accountdetails()

    elif choice == "2":
        account.checkbalance()

    elif choice == "3":
        amount = float(input("Enter Deposit amount: "))
        account.deposit(amount)

    elif choice == "4":
        amount = float(input("Enter Withdraw amount: "))
        account.withdraw(amount)

    elif choice == "5":
        print("Thank you for using the system")
        break

    else:
        print("Invalid choice")