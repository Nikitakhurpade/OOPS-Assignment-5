class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        sum = self.num2 + self.num1
        return sum
    def subtract(self):
        substraction = self.num2 - self.num1
        return substraction
    def multiply(self):
        multiplication = self.num2 * self.num1
        return multiplication
    def divide(self):
        division = self.num2 / self.num1
        return division
num1=int(input("Enter num 1: "))
num2=int(input("Enter num 2: "))
obj = Calculator(num1,num2)
print('Addition of Entered two Numbers : ',obj.add())
print('Subtrction of Entered two Numbers : ',obj.subtract())
print('Multiplication of Entered two Numbers : ',obj.multiply())
print('Division of Entered two Numbers : ',obj.divide())