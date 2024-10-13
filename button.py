import tkinter as tk

# Initialize the count variable
count = 0

def on_button_click():
    global count  # Declare count as global to modify it
    count += 1    # Increment the count by 1
    print(f"clicks: {count}")
    

# Create the main window
root = tk.Tk()
root.title("Clicker")

# Create a button widget
button = tk.Button(root, text="Click Me!", command=on_button_click)

# Pack the button onto the window
button.pack(pady=20)

# Start the main event loop
root.mainloop()
