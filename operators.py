                      #Arithmetic Operators
num1 = 34
num2 = 10

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 % num2) # modulus - Returns the ramainder

#Comparison Operators
print(num1 < num2)
print(num1 > num2)
print(num1 <= num2)
print(num1 >= num2)
print(num1 == num2) # Equal to
print(num1 != num2) # Not equal to

#Assignment Operators
number = 12
print(number)

number += 2 #Operator precedence (just like BODMAS) thus Assignment happens first then the addition
print(number)

b = 56
b -=1 # assignment (=) should happen first before the minus
print(b)

#Logic Operators- and,or, not
print(34 < 10 and 89 > 5) # An 'and' returns true if all the conditions are true
print(34 < 10 or 89 > 5) # An 'or' returns a true if any of the conditions are true
print(not( 34 < 10 or 89 > 5)) # A 'not' reverses the results used in 'or'
print(34 < 10 and 89 > 5)