class Point:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def square(self):   
        a= self.x**2
        b= self.y**2
        c= self.z**2
        return a,b,c
    def sqSum(self):
        square_sum = self.x**2 + self.y**2 + self.z**2
        return square_sum
num1=int(input("Enter num 1: "))
num2=int(input("Enter num 2: "))
num3=int(input("Enter num 3: "))
obj=Point(num1,num2,num3)
print('Square of Entered Number : ',obj.square())
print('Square Sum of Entered Number :',obj.sqSum())


