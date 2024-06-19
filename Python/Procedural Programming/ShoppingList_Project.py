def showHelp():
    print("Enter HELP to show this help message")
    print("Enter the name of the items you want to buy")
    print("Enter SHOW to show your current list")
    print("Enter DONE to finalise your shopping list")

def getNumItems(list):
    return (len(list))

def addItem(list, temp):
    list.append(temp)
    print("You now have {} items in your shopping list".format(getNumItems(list)))  # This will print the number of items

def printList(list):
    print("Your shopping list is: ")
    temp = 1
    for x in list:
        print(f"{temp}) {x}")  # using f-string
        temp += 1

ShoppingList = []
showHelp()
while(1):
    
    temp = input("Next Input: ")
    if(temp == "DONE" or temp == "done"):
        break
    elif(temp == "HELP" or temp == "help"):
        showHelp()
    elif(temp == "SHOW" or temp == "show"):
        printList(ShoppingList)
    else:
        addItem(ShoppingList, temp)

printList(ShoppingList)