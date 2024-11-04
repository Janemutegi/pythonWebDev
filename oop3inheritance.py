#Parent class
class Animal:
    def speak(self):
        print("Animal is speaking")
#Child Class
class Dog(Animal):     # Demonstrating inheritance
    def bark(self):
        print("Dog is barking")

        #Demonstrating inheritance
#To have Dog acquiring what Animal has ie speaks and barks

a = Animal()
d = Dog()
d.speak()

#Read more on inheritance e.g
# one child one parent
#Multi-level inheritance
#two child class one parent