import tkinter as tk

def hello():
    print("Hello!")

def goodbye():
    print("Goodbye!")

# Create the main window
root = tk.Tk()
root.title("Menu Example")

# Create a Menu
menu_bar = tk.Menu(root)

# Create a File menu with some options
file_menu = tk.Menu(menu_bar, tearoff=0)  # tearoff=0 removes the dashed line at the top
file_menu.add_command(label="Open", command=hello)
file_menu.add_command(label="Save", command=hello)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)

# Create an Edit menu with some options
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut", command=hello)
edit_menu.add_command(label="Copy", command=hello)
edit_menu.add_command(label="Paste", command=hello)

# Create a Help menu with a cascaded submenu
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=hello)

# Use the cascade method to add cascading menus
menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
menu_bar.add_cascade(label="Help", menu=help_menu)

# Configure the root window to use the menu bar
root.config(menu=menu_bar)

# Run the Tkinter event loop
root.mainloop()
