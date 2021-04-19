class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
    def getBalance(self):
        return self.balance
    
    def deposit(self, amount):
        self.balance = self.balance + amount
    
    def withdrawal(self, amount):
        self.balance = self.balance - amount

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate

    def interestAmount(self):
        a = self.balance * self.interestRate / 100
        return a

p1 = SavingsAccount("Mark", 2000, 5)
print (p1.getBalance())
p1.deposit(500)
print (p1.getBalance())
p1.withdrawal(500)
print (p1.getBalance())
print (p1.interestAmount())