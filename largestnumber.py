#from datatype import second

first = int(input("Enter first number: "))
second= int(input("Enter second number: "))
third = int(input("Enter third number: "))

if first > second and first > third:
    print("First number is greater")

elif second > first and second > third:
    print("Second number is greater")
else:
    print("Third number is greater")
