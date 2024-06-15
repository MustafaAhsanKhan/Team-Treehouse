import sys
attempts = 1

num = int(input("Enter an integer: "))
while(num <= 0):
    if(attempts == 3):
        sys.exit("You have exceeded the number of attempts.")
    num = int(input("Enter an integer greater than 0: "))
    attempts += 1

print("You entered: {}".format(num))