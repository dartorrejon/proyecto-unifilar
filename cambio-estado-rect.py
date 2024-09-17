# prompt: Crear ventana con Tkinter donde se dibuje un rectangulo horizontal verde al apretar un boton 1 pero el rectangulo se ponga vertical y rojo al soltar el boton 1

import tkinter as tk

# Create the main window
root = tk.Tk()

# Create the canvas
canvas = tk.Canvas(root, width=200, height=100)
canvas.pack()

# Create the rectangle
rectangle = canvas.create_rectangle(50, 20, 150, 80, fill="green")

# Define a function to change the rectangle's color and orientation when the mouse button is pressed
def on_mouse_down(event):
    canvas.itemconfig(rectangle, fill="red")
    canvas.coords(rectangle, 20, 50, 80, 150)

# Define a function to change the rectangle's color and orientation when the mouse button is released
def on_mouse_up(event):
    canvas.itemconfig(rectangle, fill="green")
    canvas.coords(rectangle, 50, 20, 150, 80)

# Bind the mouse button events to the functions
canvas.bind("<Button-1>", on_mouse_down)
canvas.bind("<ButtonRelease-1>", on_mouse_up)

# Start the main loop
root.mainloop()
