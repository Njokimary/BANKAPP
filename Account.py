class BankAccount:
    def __init__(self, acc_number, acc_name, initial_balance):
        self.acc_number = acc_number
        self.acc_name = acc_name
        self.balance = initial_balance

    def deposit(self,amount):
        self.balance += amount

    def check_balance(self):
        print(f"Hello {self.acc_name},Your Balance is {self.balance}")

    def withdraw(self,amount):
        if 0 < amount <= self.balance:
            self.balance -=amount
            print(f"hello {self.acc_name} Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")


Njoki = BankAccount(11111,"njoki mary",0)
Njoki.deposit(10000)
Bin = BankAccount(22222,"Bin Amin",12000)
print(Njoki.balance)
print(Bin.balance)
Bin.deposit(20000000)
# print(Bin.balance)
# print(Njoki.check_balance())
Njoki.withdraw(5000)
