temperatures = []  # Empty list

temperatures.append(30)  # Adds an element to the end(right) of the list
temperatures.append(33)

print(temperatures)

temperatures_2 = [40, 43]

temperatures.extend(temperatures_2)  # Combining the two lists  # into temperatures

print(temperatures)  

ints = [1, 2, 3, 4, 5]

ints_2 = [6, 7, 8, 9, 10]

ints_3 = ints + ints_2  # Combining the two lists  # into ints_3  # Hence, the original lists remain unchanged

print(ints_3)

# Lists can have multiple data types in them at once

# List[index] # Python is 0 indexed meaning the first element is stores at the 0th index

# List[-index] # -1 as the index will give the last element # -2 as the index will give the second last element and so on

ints.insert(2, 0)  # This will insert the number "0" at the 2nd index and move all others elements forward  # Previous elements stay in their position

print(ints)

temp = ints[0]

del ints[0]  # Removing the element at the 0th index

print(ints)

print(temp)  # The copy does NOT get deleted

# another way is using the .pop() method  # by default it pops the last(right-most) index

temp = ints.pop()  # You can specifiy which index you want to remove  # pop(0)
# The way this is different is that the assignment and deletion are happening in the same step

print(temp)

print(ints)

str = "This is a string"

words = str.split()  # This splits the setence into words and stores it in a list

print(words)

new_str = ": ".join(words)  # The reverse can be done using the .join() method  # The calling object is the seperator. In this case ": "

print(new_str)

words = new_str.split(": ")  # You can pass the delimiter as an argument

print(words)

# MULTIDIMENSIONAL LISTS #

# 2D List #

coordinates = [[0,5], 
               [1,1], 
               [2,2], 
               [3,3]]  # This is a list having 4 rows and 2 columns

print(len(coordinates))  # This prints the top level dimension
# For example in a 3D list (3x4x5), len would give 3


threeD_list = [
    [  # First 2D list
        [1, 2, 3],
        [4, 5, 6]
    ],
    [  # Second 2D list
        [7, 8, 9],
        [10, 11, 12]
    ]
]

print(len(threeD_list))  # 2x2x3

# Now to get an element we need to specify the indexes

print(coordinates[0][1])  # 0th row 1st columns