# Write a program to create a base class Bird, with a constructor and two methods. Then, create a child class that inherits the constructor from Class Bird and has two functions. Finally, display how you can use Super to access the parent class constructor inside the child clas
class BIRD:
    def __init__(self):
        print("bird ready now u die")
    def birdactions(self):
        print("bird action = fly, crap on car")
    def birdswim(self):
        print("bird swims and craps in water")
class Eagle(BIRD):
    def __init__(self):
        super().__init__()
        print("eagle is ready to crap on you")
    def yolo(self):
        print("begin operation crap on floor")
    def eaglefly993(self):
        print("crap")
Feather = Eagle()
# how to cawl r method ss using objn ects
Feather.birdswim()
Feather.birdactions()
Feather.yolo()
Feather.eaglefly993()