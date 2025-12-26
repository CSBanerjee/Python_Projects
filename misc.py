class BankAccount:
    def __init__(self,name,balance=0):
        self.name = name
        self.balance = balance
    
    def deposit(self,amount):
        self.balance +=amount 
    
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance -=amount 
    
    def get_balance(self):
        return self.balance

acc = BankAccount("Chandra",1000)
acc.deposit(1000)
acc.withdraw(300)
total = acc.get_balance()
print(total)