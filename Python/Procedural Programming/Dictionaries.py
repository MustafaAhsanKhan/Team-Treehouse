course = ["OOP", "Mustafa", "2nd"]

# Now to convert this list into a dictionary we will use curly brackets

course = {"Title":"OOP", "Teacher":"Mustafa", "Semester":"2nd"}

print(course["Title"])  # We access values using the keys

print(course.keys())  # Prints all the keys

print(course.values())  # Prints all the values

for x in course:  # This will print the keys
    print(x)

print()

for key, value in course.items():  # This uses multiple assignment to store the elements of the tuple
    print(key)
    print(value)

# We can use the concept of packing and unpacking in dictionaries aswell

def print_teachers(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_teachers(Name = "Mustafa", Job = "Professor", Topic = "Maths")

teacher = {
  'Name':'Ashley',
  'Job':'Instructor',
  'Topic':'Python'
}

def print_teacher2(name, job, topic):
    print(name)
    print(job)
    print(topic)

print_teachers(**teacher)  # This will unpack the "teacher" dictionary