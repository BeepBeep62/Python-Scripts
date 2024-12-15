import tkinter as tk
from random import randint

class GoreEngine:
    def __init__(self, master):
        self.master = master
        self.master.title("GORE Engine")

        # Canvas setup
        self.canvas = tk.Canvas(self.master, width=800, height=600, bg="black")
        self.canvas.pack()

        # Shape storage
        self.shapes = []  # Stores tuples of (shape_id, shape_type)

        # Bind events
        self.canvas.bind("<Button-1>", self.create_random_shape)
        self.canvas.bind("<B1-Motion>", self.drag_shape)

        self.selected_shape = None  # Store the shape being dragged

    def create_random_shape(self, event):
        shape_type = randint(1, 3)  # 1=rectangle, 2=circle, 3=line

        if shape_type == 1:  # Rectangle
            x1, y1 = event.x - 30, event.y - 30
            x2, y2 = event.x + 30, event.y + 30
            color = self.random_color()
            shape_id = self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)
            self.shapes.append((shape_id, "rectangle"))

        elif shape_type == 2:  # Circle (oval)
            x1, y1 = event.x - 30, event.y - 30
            x2, y2 = event.x + 30, event.y + 30
            color = self.random_color()
            shape_id = self.canvas.create_oval(x1, y1, x2, y2, fill=color, outline=color)
            self.shapes.append((shape_id, "circle"))

        elif shape_type == 3:  # Line
            x1, y1 = event.x - 50, event.y
            x2, y2 = event.x + 50, event.y
            color = self.random_color()
            shape_id = self.canvas.create_line(x1, y1, x2, y2, fill=color, width=3)
            self.shapes.append((shape_id, "line"))

    def drag_shape(self, event):
        if not self.selected_shape:
            self.selected_shape = self.canvas.find_closest(event.x, event.y)[0]

        # Move the selected shape
        if self.selected_shape:
            self.canvas.coords(self.selected_shape, event.x - 30, event.y - 30, event.x + 30, event.y + 30)

    def random_color(self):
        return f"#{randint(0, 255):02x}{randint(0, 255):02x}{randint(0, 255):02x}"

if __name__ == "__main__":
    root = tk.Tk()
    app = GoreEngine(root)
    root.mainloop()
