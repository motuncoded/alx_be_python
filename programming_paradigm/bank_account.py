class BankAccount:
    def __init__(self, initial_balance=0):
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return f"Deposited: ${amount:.1f}"

    def withdraw(self, amount):
        if amount <= self.__account_balance:
             self.__account_balance -= amount
             print(f"Withdrew: ${amount:.1f}")
             return True
        else:
            print("Insufficient funds.")
            return False
    

    def display_balance(self):
        return f"Current Balance: ${self.__account_balance:.2f}"
