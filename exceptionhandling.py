# An exception is an error in programming
# Try block test a program is about to encounter an error
# Except block
# Finally block

#from variables import number
#from operators import number

#print(number) # error coz no value assigned to the variable
# Thus with line 5 it sorts the problem getting the variable from a python file(variables) with the value

#Try block
try:
    print(number)
except:
    print("An error has occurred")


try:
    num1 = 45
    num2 = 0
    print(num1 / num2)

except:
    print("A ZeroDivisionerror has occurred")

finally:
    print("Succeed")# It prints regardless presence of an error or not