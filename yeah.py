import turtle
turtle.Screen().setup(420,380)
turtle.Screen().bgcolor("dark blue")
turtle.color("light blue")
turtle.pensize(5)
turtle.goto(0,0)
for i in range(5):
    turtle.circle(3)
    turtle.forward(100)
    turtle.left(130)
    turtle.circle(3)
    turtle.forward(100)
    turtle.left(90)
turtle.done()