class Student:
    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setRollNumber(self, rollNumber):
        self.__RollNumber = rollNumber

    def getRollNumber(self):
        return self.__RollNumber


std = Student()
std.setName("Alex")
std.setRollNumber("3789")
print (std.getName())
print (std.getRollNumber())
