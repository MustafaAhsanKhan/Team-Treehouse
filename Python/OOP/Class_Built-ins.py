class Laptop:
    def __init__(self, company, year):
        self. company = company
        self.year = year

    def __str__(self):
        return f"The company is {self.company}. The model year is {self.year}"
    
    def __eq__(self, other):  # This is a function that allows us to compare two objects using the "==" operator
        if(self.company == other.company):
            if(self.year == other.year):
                return True
            
        return False
    

lap1 = Laptop("DELL", 2024)
lap2 = Laptop("DELL", 2023)

print(lap1 == lap2)  # using the __eq__ method

print(lap1)  # The __str__ method has replaced the default print that outputs a memory location


class Dealership:
    def __init__(self):
        self.cars = ["Ford", "Honda", "Bugatti"]

    def __iter__(self):
        yield from self.cars  # Returns each element in the attribute


my_dealership = Dealership()

for car in my_dealership:  # The __iter__ method allows an object of a class to be iterated over
    print(car)