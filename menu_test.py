
import tkinter as tk

def on_file_menu_click():
    print("File menu clicked!")
    # Add your desired functionality here

# Create the main application window
root = tk.Tk()
root.title("Menu Click Example")

# Create a menu bar
menu_bar = tk.Menu(root)

# Create a File menu
file_menu = tk.Menu(menu_bar, tearoff=0)

# Add a menu item to the File menu with the desired function
file_menu.add_command(label="File Action", command=on_file_menu_click)

file_menu1 = tk.Menu(menu_bar, tearoff=0)

# Add a menu item to the File menu with the desired function
file_menu1.add_command(label="File Action1", command=on_file_menu_click)

# Set the menu bar for the root window
root.config(menu=file_menu)
root.config(menu=file_menu1)
# Run the Tkinter event loop
root.mainloop()
