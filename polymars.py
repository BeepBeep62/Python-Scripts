import turtle
turtle.Screen().bgcolor("blue")
turtle.Screen().setup(600,600)
polymars = turtle.Turtle()
side = 10
angle = 360/side
sidelength = 30
for i in range(side):
    polymars.forward(sidelength)
    polymars.right(angle)
turtle.done()