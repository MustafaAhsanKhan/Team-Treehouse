def PrintList(list):  # A function that prints all the elements in the list that is passed as the argument
    for x in list:
        print(x)
    print()

for x in range(0, 3):  # (start, stop, step_size)
    print(x)

str = "test string"

for i in str:  # Selects each character in the string and prints it
    print(i.upper())

ints = [0,1,2,3,4,5]

PrintList(ints)

Cities = ["Islamabad", "Peshawar", "Karachi"]

PrintList(Cities)

# Lists ARE passed as reference # So any changes made in the function are reflected in the original list

rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

for index, x in enumerate(rainbow, 5):  # This is another method to print lists  # You can even define the starting index
    print(f"{index}) {x}")  # Using f-strings