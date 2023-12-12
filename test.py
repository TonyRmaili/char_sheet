import tkinter as tk

def toggle_color():
    current_color = canvas.itemcget(circle, "fill")
    new_color = "green" if current_color == "white" else "white"
    canvas.itemconfig(circle, fill=new_color)

root = tk.Tk()
root.title("Toggle Color Example")

canvas = tk.Canvas(root, width=100, height=100, bg="white")
canvas.pack(padx=10, pady=10)

circle = canvas.create_oval(10, 10, 90, 90, outline="black", fill="white")
canvas.tag_bind(circle, "<Button-1>", lambda event: toggle_color())

root.mainloop()
