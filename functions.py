# Built-in Functions

#max function
y = max(34,56,70,18)
print(y)
#min
x = min(40,67,34,25,50)
print(x)

# To return the power of the value
z = pow(2,3)
print("The results is", z)

#user-defined functions- unatengeneza function yako
def greeting():
    print("Hello there")

greeting() # Calling the Function

def multiply():
    a = 12
    b = 10
    print(a * b)

multiply()

# Parameters and Arguments- to enable working with various values than restriction to 10 and 12 above
# Parameter/Variable
# Argument/ Value

def add(x , y):
    print(x + y)

add(4,5)
add(60 ,10)

def multiplys(a, b):
    print(a * b)
multiplys(40,5)

def employee(fullname,age,position,status):
    print(fullname,age,position,status)
employee("Diana",29,"CEO", "Single")
employee("Jack",40,"SArchitect", "Single")
employee("Jane",44,"Administrator", "Married")
employee("Bernard",42,"Digital Marketer", "Single")
employee("Evelyne",36,"Accountant", "Married")


