                                                     #from doctest import set_unittest_reportflags

#from variables import lastname

firstname = input("Enter your first name: ")
print("My first name is",firstname)
lastname = input("Enter your lastname: ")
print("My surname is", lastname)
surname = input("Enter your surnames: ")
print("My full name is",firstname,lastname,surname)

age = int(input("Enter your age: "))
print("I am", age, "years old")

weight = float(input("Enter your weight: "))
print("My weight is", weight)

temperature = int(input("Enter your temperature: "))

if temperature > 25:
    print("It is too hot")
else:
    print("It is too cold")