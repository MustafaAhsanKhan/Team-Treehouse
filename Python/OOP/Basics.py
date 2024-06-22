class Car:  # This is the class
    # Attributes
    wheels = 4
    doors = 4
    engine = True

    def __init__(self, make, model, year = 0):  # This is the constructor  # 0 is the default value for year
        self.make = make
        self.model = model
        self.year = year

    def setSpeed(self, speed):
        self.speed = speed
        print(f"The new speed is {speed}")


myCar = Car("Honda", "Civic", 2024)  # We need to pass in the make model and year

print(isinstance(myCar, Car))  # This can be used to check if an object is of the specified class datatype

print(myCar.doors)  # We can access attributes of an object this way

myCar.doors = 2  # This will change the number of doors for only this instance, not other objects

myCar.setSpeed(50)


# Another example
class Panda:
    species = 'Ailuropoda melanoleuca'
    food = 'bamboo'

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True
        
    def check_if_hungry(self):
        if self.is_hungry:
            self.eat()
        
    def eat(self):
        self.is_hungry = False
        return f"{self.name} eats {self.food}."