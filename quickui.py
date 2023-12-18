import tkinter as tk

def dummy_command():
    print("This is a dummy command.")

def main():
    root = tk.Tk()
    root.title("Cascading Menus Example")

    # Create the menu bar
    menubar = tk.Menu(root)

    # Create the File menu
    file_menu = tk.Menu(menubar, tearoff=0)
    file_menu.add_command(label="New", command=dummy_command)
    file_menu.add_command(label="Open", command=dummy_command)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.destroy)
    menubar.add_cascade(label="File", menu=file_menu)

    # Create the Edit menu
    edit_menu = tk.Menu(menubar, tearoff=0)
    edit_menu.add_command(label="Cut", command=dummy_command)
    edit_menu.add_command(label="Copy", command=dummy_command)
    edit_menu.add_command(label="Paste", command=dummy_command)
    menubar.add_cascade(label="Edit", menu=edit_menu)

    # Create a submenu for Edit menu
    sub_menu = tk.Menu(edit_menu, tearoff=0)
    sub_menu.add_command(label="Subcommand 1", command=dummy_command)
    sub_menu.add_command(label="Subcommand 2", command=dummy_command)
    edit_menu.add_cascade(label="Submenu", menu=sub_menu)

    # Configure the root window to use the menu bar
    root.config(menu=menubar)

    root.mainloop()

if __name__ == "__main__":
    main()
