name = input("Enter your name: ")  # Taking an input

print("Hello " + name + "!" * 20)  # Concatenation  # Multiplying the string "!" 20 times

str = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."

str.upper()  # Converting the string to uppercase

str.lower()  # Converting the string to lowercase

str.title()  # Converting the string to title case

str.capitalize()  # Capitalizing the first letter of the string

print(str)  # The original string remains unchanged
# So you need to store the result of the operation in a variable

new_str = str.upper()  # Storing the result of the operation in a variable

print(new_str)  # The new string is printed

template = "Hello, my name is {} and I am {} years old."  # A template string

print(template.format("John", 25))  # Filling in the template with the values

print("ham" in "Hamburger")  # Checking if the string contains a substring