class Student:
    __name = ""
    __rollNumber = ""

    def setName(self,name):
        self.__name = name
    def getName(self):
        return self.__name
    def setRollNumber(self,rollNumber):
        self.__rollNumber = rollNumber
    def getRollNumber(self):
        return self.__rollNumber
obj=Student()
obj.setName("Nikita")
print('Name of the sudent : ',obj.getName())
obj.setRollNumber(17)
print("RollNumber of the student : ",obj.getRollNumber())