class BankAccount:
    def __init__(self, account_balance):
        self.__account_balance = account_balance
        
        
    def get_account_balance(self):
        return self.__account_balance
    def set_account_balance(self, account_balance):
        if account_balance > 0:
            self.__account_balance = account_balance
        else:
            print("Your account balance is zero!")
    
    def deposit(self, amount):
        self.__account_balance += amount
    def withdraw(self,amount):
        if amount <= self.__account_balance:
          self.__account_balance   -= amount
          return True
        else:
            return False
    
    def display_balance(self):
        
         print(f"Current Balance: ${self.__account_balance:.2f}")