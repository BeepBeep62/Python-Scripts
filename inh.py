# Write a Python program to implement Inheritance by creating a Parent Class Vehicle with a constructor that has details like name, maximum speed, and mileage. Then, create a Child Class Bus that inherits Class Vehicle. Finally, showcase Inheritance to display the details of the Vehicle Bus named - School Volvo.
class Vehicle:
    def __init__(self, name, maximumspeed, mileage):
        self.name = name
        self.maximumspeed = maximumspeed
        self.mileage = mileage
class bus(Vehicle):
    pass
schoolbus = bus('schoolisbadbus', 600, 100)
print(schoolbus.name)