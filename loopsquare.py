import turtle
turtle.Screen().setup(600,600)
turtle.Screen().bgcolor("purple")
turtle.color("cyan")
Pen = turtle.Turtle()
size = 0
while True:
    for i in range(0,4):
        Pen.forward(size+1)
        Pen.left(90)
        size = size-5
    size = size+1
turtle.done()