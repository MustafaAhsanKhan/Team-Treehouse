#FUNCTION PACKING#

# If you look closely the arguments and parameters of a function is a tuple
# We can use this to PACK all the arguments into one tuple

def packer(*args):  # args is the tuple we store all the passed arguments in
    print(args)

packer(1,2,3,4,5)

# A use-case for packing is when you dont know the number of paramaters
# For example a shopping list, where you may have multiple items

def calculate_total(*args):
    return (sum(args))

print(calculate_total(10,20,13))  # The number of arguments can change

# Naturally unpacking does the opposite
# We return a tuple and can assign it to multiple variables

def unpacker():
    return (1,2,3)

var1, var2, var3 = unpacker() # note: The number of variables must be EXACTLY equal to the number of elements returned by the function

print(var2)