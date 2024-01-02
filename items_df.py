# import numpy as np
# import json
# import pandas as pd

# with open('./cleaned_data/items.json', 'r') as file:
#     data = json.load(file)

# df = pd.json_normalize(data['item'])

# def main(data):
#     for row in data['itemGroup']:
#          print(row)

# def del_key():
#     del data['_meta']
#     return data

# def save_data(data):
#     with open('./cleaned_data/items.json','w') as file:
#         json.dump(data, file,indent=4)
# if __name__ == "__main__":
#     data = del_key()
#     print(df.columns)
#     save_data(data)


# import tkinter as tk

# def update_selection():
#     selection_label.config(text=f"Selected option: {var.get()}")

# # Create the main Tkinter window
# root = tk.Tk()
# root.title("Exclusive Checkbuttons Example")

# # Variable to track the selected option
# var = tk.StringVar()

# # Function to update the label with the selected option
# var.trace_add("write", lambda *args: update_selection())

# # Create two Radiobuttons
# option1 = tk.Radiobutton(root, text="Option 1", variable=var, value="Option 1")
# option2 = tk.Radiobutton(root, text="Option 2", variable=var, value="Option 2")

# # Label to display the selected option
# selection_label = tk.Label(root, text="Selected option: None")

# # Place the widgets in the window
# option1.pack(pady=5)
# option2.pack(pady=5)
# selection_label.pack(pady=10)

# # Run the Tkinter event loop
# root.mainloop()

import tkinter as tk

def checkbutton1_changed():
    var2.set(0)  # Uncheck checkbutton2 when checkbutton1 is checked

def checkbutton2_changed():
    var1.set(0)  # Uncheck checkbutton1 when checkbutton2 is checked

# Create the main Tkinter window
root = tk.Tk()
root.title("Exclusive Checkbuttons Example")

# Variables to track the state of checkbuttons
var1 = tk.IntVar()
var2 = tk.IntVar()

# Create two Checkbuttons
checkbutton1 = tk.Checkbutton(root, text="Option 1", variable=var1, command=checkbutton1_changed)
checkbutton2 = tk.Checkbutton(root, text="Option 2", variable=var2, command=checkbutton2_changed)

# Place the widgets in the window
checkbutton1.pack(pady=5)
checkbutton2.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()


