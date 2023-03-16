# Implement a Calculator Class

class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        return(self.num1+self.num2)
    def subtract(self):
        return(self.num2-self.num1)
    def multiply(self):
        return(self.num1*self.num2)
    def divide(self):
        return(self.num2/self.num1)

obj=Calculator(10,94)
print("The sum is: ",obj.add())
print("The difference is: ",obj.subtract())
print("The product is: ",obj.multiply())
print("The division is: ",obj.divide())