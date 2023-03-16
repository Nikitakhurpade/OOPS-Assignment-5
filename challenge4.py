class Account:  #create class 
    def __init__(self,title=None,Balance=0):
        self.title=title
        self.Balance=Balance


class SavingsAccount(Account):  #create subclass
    def __init__(self,title,Balance,interestRate):
        self.interestRate=interestRate
        super().__init__(title,Balance)
        
    def display(self): 
      return(f" Account Holder Name : {self.title}  \n Account Balance : {self.Balance} Rs. Only \n Interest Rate : {self.interestRate} % ") 
print("Hello!!! Welcome to Indian Bank ")         
obj=SavingsAccount("Nikita",1000,5)
print(obj.display())
