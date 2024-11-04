# A list can carry values of different datatypes e.g int,booleans,strings,floats
# In arrays can carry value of same datatype

courses = ["MIT", "Datascience", "Cybersecurity"]
print(courses)
print(courses[1])
print(courses[2])
print(courses[0])
# This accessing an element in an array

# looping through an array
for course in courses:
    print("The course includes", course)
    print("The course includes", course)

# Adding a new element
courses.append("Android development")
print(courses)
for course in courses:
    print("The course includes", course)

# Deleting an element
courses.remove("MIT")
print(courses)

