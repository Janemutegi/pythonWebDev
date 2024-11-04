Topic = "A Simple Calculator Python Program"
print(Topic)
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number:"))
print("The operation to use: '*' , '+' , '-' and '/'")
operation = input("Enter the operator:")


if operation == "+":
    print(num1+num2)
elif operation == "-":
    print(num1-num2)
elif operation == "*":
    print(num1*num2)
elif operation == "/" :
    if num2 !=0:
        print(num1/num2)
    else:
        print("error")

