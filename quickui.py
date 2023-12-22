import tkinter as tk

def draw_circle(canvas):
    # Center coordinates and radius of the circle
    x, y, radius = 50, 50, 7
    
    # Draw the circle on the canvas
    return canvas.create_oval(x-radius, y-radius, x+radius, y+radius, fill="blue")

def toggle_circle(canvas, circle_id):
    # Toggle the visibility of the circle
    current_state = canvas.itemcget(circle_id, "state")
    new_state = "hidden" if current_state == "normal" else "normal"
    canvas.itemconfigure(circle_id, state=new_state)

# Create the main window
root = tk.Tk()
root.title("Toggle Circle")

# Create a canvas widget
canvas = tk.Canvas(root, width=100, height=100, bg="red")
canvas.pack()

# Draw the initial circle on the canvas
circle_id = draw_circle(canvas)

# Create a button to toggle the circle
toggle_button = tk.Button(root, text="Toggle Circle", command=lambda: toggle_circle(canvas, circle_id))
toggle_button.pack()

# Start the Tkinter event loop
root.mainloop()

