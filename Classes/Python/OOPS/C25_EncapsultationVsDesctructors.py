#Without Encapsulation

'''This way there is no control anyone can modify any value.
Asal data ki protection eh ledu'''
class WithOutEncap:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []
        self.enrolled = True

exObj1 = WithOutEncap("Pranith",1)
exObj1.grades.append(90)
exObj1.enrolled = False
exObj1.name = "Sai Pranith"
#print(exObj1.__dict__)

#With Encapsulation
class WithEncap:
    def __init__(self, name, student_id):
        self.__name = name
        self.__student_id = student_id
        self.__grades=[]
        self.__enrolled = True

exObj2 = WithEncap("Pranith",1)
exObj2._WithEncap__grades.append(90) #This way it modifies the same attribute
exObj2.__enrolled = False #This way it creates a new attribute __enrolled
exObj2.__name = "Sai Pranith"
#print(exObj2.__dict__)


#------------------------------------------------------------------------------------
class Student:
    def __init__(self, name, student_Id):
        self.__name = name
        self.__student_Id = student_Id
        self.__grades = []
        self.__enrolled = True
    def add_grade(self,grades):
        if not self.__enrolled:
            return "Cant add grade as student not enrolled"
        self.__grades.append(grades)
    def get_info(self):
        return {
            "name": self.__name,
            "student_id": self.__student_Id,
            "grades": self.__grades,
            "enrolled": self.__enrolled
        }

student1 = Student("Pranith", 1)
student1.add_grade(95)
student1.add_grade(99)
print(student1.get_info())