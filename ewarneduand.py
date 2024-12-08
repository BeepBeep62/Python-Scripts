# Write a program to create a class Point that consists of a constructor to set coordinates equal to x and y. Also, it consists of a function that returns the coordinates in Point format. Create an object passing the coordinates and print the Point.
class point:
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y
    def __str__(self) -> str:
        return "({0},{1})".format(self.x, self.y)
cordinade = point(5,6)
print(cordinade)