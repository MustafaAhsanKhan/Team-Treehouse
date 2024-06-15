def getNumItems(list):
    return (len(list))

def addItem(list):
    list.append(input("Enter the item you want to buy: "))
    print("You now have {} items in your shopping list".format(getNumItems(list)))  # This will print the number of items

def printList(list):
    print("Your final shopping list is: ")
    temp = 1
    for x in list:
        print(f"{temp}) {x}")  # using f-string
        temp += 1

ShoppingList = []
while(1):
    addItem(ShoppingList)
    temp = input("Do you want to continue? Y/N: ")
    if(temp == "N" or temp == "n"):
        break

printList(ShoppingList)