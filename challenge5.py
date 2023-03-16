class Account:
    def __init__(self,title=None,balance=0):
        self.title=title
        self.balance=balance
    def withdrawl(self,amount):
        self.balance=self.balance-amount 
    def deposit(self,amount):
        self.balance=self.balance+amount
    def getBalance(self):
        return self.balance
class SavingsAccount(Account):
    def __init__(self,title=None,balance=0,interestRate=0):
        super().__init__(title,balance)
        self.interestRate=interestRate
    def interestAmount(self):
        interestAmount=self.balance*self.interestRate/100
        return(self.balance*self.interestRate/100)

demo1=SavingsAccount("Nikita",2000,5)
print("Initial balance: ",demo1.getBalance())
demo1.deposit(500)
print("Updated balance after deposit: ",demo1.getBalance())
demo1.withdrawl(500)
print("Updated balance after withdrawal: ",demo1.getBalance())
print("Interest amount is: ",demo1.interestAmount())