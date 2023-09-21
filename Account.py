    # CLASS
    # INSTANCE
    # Class attributes & methods
    # instance attributes & methods
    # inheritance
    # decorator

# instance method - deposit  that takes amount
# self.initial balance

# Savings account
# subClass => SavingsAccount



class Bank_accounts:
    total_balance = 0

    def __init__(self,acc_number,acc_name,balance):
        self.acc_number = acc_number
        self.acc_name = acc_name
        self.balance = balance
        Bank_accounts.total_balance += self.balance
    
    @classmethod
    def total_bank_balance(cls):
            print(cls.total_balance)

    def deposit(self, amount):
        self.balance += amount
        Bank_accounts.total_balance += amount


    def check_balance(self):
        print(f'Hello {self.acc_name}, Your current balance is {self.balance}')

    def withdraw(self,amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f'Hello {self.acc_name},You have successfully withdrawn Ksh {amount}. Your current balance is {self.balance}')
        else:
            print("Insufficient balance")


class Savings_account(Bank_accounts):
        
        def add_interest(self):
            self.balance *= 1.03


Bin = Bank_accounts(122334422,"Bin Amin",0)
Dan = Bank_accounts("122223334423","Danwycliff",5000)
Bin.deposit(60000)

print(Bank_accounts.total_bank_balance())