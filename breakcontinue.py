# Break statement is usually used to exit an entire loop or stop a program upon reaching a given value in a range

# Break statement

num = 20
while num <= 25:
    print(num)
    if num == 23:
        break
    num += 1 # incrementing the value by 1

# Continue Statement
#list
devices = ["laptop", "phone", "tablet"]
for device in devices:
    if device == "laptop":
        continue # Continue 'skips' a loop
    print(device)

