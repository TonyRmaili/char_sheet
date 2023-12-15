import tkinter as tk
from tkinter import ttk

def on_combobox_select(event):
    selected_item = combobox.get()
    print(f"Selected Item: {selected_item}")

def reset_widgets():
    entry.delete(0, tk.END)  # Delete all characters in the Entry widget
    combobox.set("Select an option")  # Set the Combobox to its default value

# Create the main window
root = tk.Tk()
root.title("Reset Widgets Example")

# Create an Entry widget
entry = tk.Entry(root)
entry.pack(pady=10)

# Create a Combobox
combobox = ttk.Combobox(root, values=["Option 1", "Option 2", "Option 3"])
combobox.pack(pady=10)
combobox.set("Select an option")

# Bind a function to handle selection events
combobox.bind("<<ComboboxSelected>>", on_combobox_select)

# Create a button to trigger the reset
reset_button = tk.Button(root, text="Reset Widgets", command=reset_widgets)
reset_button.pack(pady=10)

# Run the main loop
root.mainloop()
