#class is blueprint of an object-got from a class
#create a class for Evans and Janet

class Student:
#Properties/Variables/Attributes/Characteristics
    name = ("Evans")
    gender = ("Male")
    age = 32
# Behaviours/Method/Function
    def study(self):
        print("Student is studying")

        #Creating/Instantiating an object(student1)
student1 = Student()
student1.study()
print(student1.name)

        ##Creating/Instantiating an object(student2)
student2 = Student()
print(student2.name)
# So we need to be able to print various names for the students in oop2.py

