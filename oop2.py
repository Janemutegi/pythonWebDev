#Working with different values in object oriented
class Person:
# Class must have either properties and behaviour or all
#properties/variables
    def __init__(self, name,gender,age):# Self is the default object of a class
        self.name = name
        self.gender = gender
        self.age = age

#Behaviours
    def movement(self):
        print("Person is walking")

person1 = Person("Evans","Male",33)
print(person1.name)

person2 = Person("Mary","Female",29)
print(person2.name)

person3 = Person("Charles", "Male","40")
print(person3.name)

#**Learn more on polymorphetus and inheritance
