class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.__balance = balance
    
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"Amount deposited successfully {amount}")
        else:
            print("Invalid amount or should be positive amount")

    def withdraw(self,amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Amount withdrawn successfully {amount}")
        else:
            print("Insufficient balance") 

    def get_balance(self):
        return self.__balance
    
    def __str__(self):
        return f"Account[{self.account_number}] - {self.account_holder} - Balance: ${self.__balance:.2f}"

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance, interest_rate):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.get_balance() * (self.interest_rate / 100)
    
    def __str__(self):
        return f"SavingsAccount[{self.account_number}] - {self.account_holder} - Balance: ${self.get_balance():.2f} - Interest Rate: {self.interest_rate}%"
    
class CurrentAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance, overdraft_limit):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.get_balance() + self.overdraft_limit:
            self._BankAccount__balance -= amount
            print(f"${amount} withdrawn successfully (with overdraft).")
        else:
            print("Withdrawal exceeds overdraft limit.") 

    def __str__(self):
        return f"CurrentAccount[{self.account_number}] - {self.account_holder} - Balance: ${self.get_balance():.2f} - Overdraft Limit: ${self.overdraft_limit}"
    
# Create accounts
savings = SavingsAccount("001", "Pranith", 1000, 4.5)
current = CurrentAccount("002", "Manasa", 500, 300)

# Savings Account
savings.deposit(200)
savings.withdraw(150)
print(savings)
print(f"Interest: ${savings.calculate_interest():.2f}\n")

# Current Account
current.deposit(100)
current.withdraw(800)
current.withdraw(200)
print(current)