class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
    
    def display(self): 
      return(f"Account Holder Name : {self.title}\nAccount Balance : {self.balance} Rs. Only ")
    def withdrawal(self, withdrawal_amount):
        self.withdrawal_amount = withdrawal_amount
        if self.balance>= withdrawal_amount:
           self.balance = self.balance - self.withdrawal_amount
        
        else:
            print("\nSorry !! You have Insufficient Balance","\nAvailable Balance :" ,self.balance,'Rs. Only')
            print('Try Again..!!')
            exit()
      
    def deposit(self, deposit_amount):
        self.deposit_amount = deposit_amount
        self.balance = self.balance + self.deposit_amount

    def getbalance(self):
        return self.balance

class SavingsAccount(Account):
    def __init__(self,title=None,balance=0,interestRate=5):
        super().__init__(title, balance)
        self.balance = balance
        self.interestRate = interestRate

    def interestAmount(self):
        self.interest_amount = (self.interestRate * self.balance)/100
        return self.interest_amount
    def display(self): 
      return(f"Interest Rate : {self.interestRate} % ")
print("Hello!!! Welcome to Indian Bank ")    
name=input('Please Enter Your Full Name : ')
print('Bank Account Details : ')
obj=Account(name,10000)
print(obj.display())
deposit_amount =int (input("Enter Amount to be Deposited : "))
obj.deposit(deposit_amount)
print("After deposit:Total Amount is : ",obj.getbalance(),'Rs.')
withdrawal_amount =int (input("Enter Amount to be Withdrawn :"))
obj.withdrawal(withdrawal_amount)
print("After withdrawal: Net Available Balance is :",obj.getbalance(),'Rs.')
print('Saving Account Details : ')
obj=SavingsAccount(name,10000,5)
print(obj.display())
print("Interest Amount : ",obj.interestAmount() ,'Rs. ')