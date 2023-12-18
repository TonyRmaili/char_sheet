import tkinter as tk

class MenuHandler:
    def __init__(self,root,label):
        self.root = root
        self.menu = tk.Menu(root)
        self.cascade(label)
    
    def cascade(self,label):
        self.menu.add_cascade(label=label,menu=)

    def create_label(self,root,text,row,column):
        label = tk.Label(master=root,text=text)
        label.grid(row=row, column=column)
    
    def create_entry(self,root,width,row,column):
        entry = tk.Label(master=root,width=width)
        entry.grid(row=row, column=column)