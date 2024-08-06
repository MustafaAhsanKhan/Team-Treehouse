rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

# Now theres slicing which we can use to access multiple elements in a list
# We were already using it when we did list[index]
# The full syntax is list[start:stop:step]

print(rainbow[1:4])  # Similar to ranges the stop value is exclusive of itself
# If we leave the stop value empty list[1:], then we will get the whole list till the end
# If we want to print alternate elements we can do List[::2]
# The original list isnt changed, but a new list is created

# Slicing also works with strings
name = "Mustafa"

print(name[:3])