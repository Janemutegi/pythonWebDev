from variables import lastname

number = 56 # Integer
second = 43.72 # Float
greeting = "Hello there" # String
isPythonIntresting = True # Boolean

print(number)
print(second)
print(isPythonIntresting)
print(greeting)
# Data Structures- Multiple values stored in a single valuable
cars = ["Toyota", "Nissan","Vw"] # List
#Elements in a list are always ordered and changeable (Mutable)
fruits = ("Banana","Orange","Apple","Mango") #Tuple
#The elements in a tuple are always ordered and unchangeable
#The normal brackets are used in a tuple compared to a list
countries = {"Kenya","Tunisia","Algeria","Botswana"} # Set
# The elements in the set are unordered and unchangeable
# Curly braces are used is a set
student = {
    "fistname" : "Glory",
    "lastname" : "Web",
    "age" : 23,
    "course" : "Web Development",
    "nationality" : "Kenyan",
}

#Dictionary - Key-value pair
print(cars)
print(fruits)
print(countries)
print(student)
print(student["course"])
print(type(student))
print(type(student["nationality"]))
print(type(countries))
print(type(second))

#Typecasting is process of converting one datatype to another e.g float to integer
print(float(number))
print(int(second))
