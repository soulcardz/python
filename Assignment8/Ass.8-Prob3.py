class Account:
    def __init__(self, title = None, balance = 0):
        self.title = title
        self.balance = balance


class SavingsAccount(Account):
    def __init__(self, title = None, balance = 0, interestRate = 0):
        Account.__init__(self, title, balance)
        self.interestRate = interestRate
        
p1 = SavingsAccount("Ridd", 150, 5)
print (p1.title)
