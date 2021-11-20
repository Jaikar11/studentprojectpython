# Setter and Getter Class

class Student:

    def setName(self,name):
        self.__name = name

    def getName(self):
        return self.__name

    def setRollNumber(self,rollnumber):
        self.__rollNumber = rollnumber;

    def getRollNumber(self):
        return self.__rollNumber

stu1 = Student()
stu1.setName("Aaron")
stu1.setRollNumber(1)

print("Student Name -",stu1.getName(),"\n\tStudent Roll Number",stu1.getRollNumber())


