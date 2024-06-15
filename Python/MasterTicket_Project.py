
TICKET_PRICE = 10
tickets_remaining = 100

def CalculatePrice(tickets):
    return (tickets * TICKET_PRICE)

print("Welcome to the ticket booth!")
while(tickets_remaining > 0):
    print("There are {} tickets remaining.".format(tickets_remaining))  # Tickets remaining
    print("The price of each ticket is ${}.".format(TICKET_PRICE))  # Ticket price

    name = input("Enter your name: ")

    # Buying tickets
    tickets_needed = int(input("Hey {} how many tickets do you want?: ".format(name)))
    while(tickets_needed > tickets_remaining or tickets_needed <= 0):
        tickets_needed = int(input("You can only buy {} tickets or less: ".format(tickets_remaining)))

    # Calculating price
    total_price = CalculatePrice(tickets_needed)

    print("Total due is ${}".format(total_price))

    if(input("Do you want to proceed Y/N?: ").lower()  == "y"):
        print("SOLD")
        tickets_remaining -= tickets_needed
    else:
        print("Bye", name)

print("Tickets sold out")