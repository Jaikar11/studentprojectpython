# Setter and Getter Class

class Student:
    # def __init__(self,name="None",rollNumber=0):
    #    self._name = name
    #    self._rollnumber = 0

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setRollNumber(self, rollnumber):
        self.__rollNumber = rollnumber;

    def getRollNumber(self):
        return self.__rollNumber


stu1 = Student()
stu1.setName("Aaron")
stu1.setRollNumber(1)

print("Student Name -", stu1.getName(), "\n\tStudent Roll Number", stu1.getRollNumber())
