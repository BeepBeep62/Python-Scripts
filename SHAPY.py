import tkinter as tk
import turtle
import time

def move_square(event):
    key = event.keysym
    if key == 'w':
        canvas.move(square, 0, -10)
    elif key == 's':
        canvas.move(square, 0, 10)
    elif key == 'a':
        canvas.move(square, -10, 0)
    elif key == 'd':
        canvas.move(square, 10, 0)
for i in range(100000000):
    turtle.circle(100)
    turtle.left(10)

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()
square = canvas.create_rectangle(190, 190, 210, 210, fill="blue")
root.bind_all('<Key>', move_square)
root.mainloop()
