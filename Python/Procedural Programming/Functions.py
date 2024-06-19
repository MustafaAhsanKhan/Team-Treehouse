def print_uppper(name):  # This is a function
    print(name.upper() + "!" * 20)

text = input("Enter your text: ")
print_uppper(text)


def split_check(total, num_people):
    if(num_people <= 0):
        raise ValueError("The number of people must be 1 or more")
    return total / num_people  # This function returns the total divided by the number of people

try:
    total_due = float(input("What is the total? "))
    num_people = int(input("How many people? "))
    print("Each person owes ${}".format(split_check(total_due, num_people)))
except ValueError as err:
    print("You must enter a number.")
    print("{}".format(err))  # This will print the error message caused from the function