import tkinter as tk
import json,os
from character import Character

folder_path = 'save_files/'
char1 = Character(name='garry',max_hp=50,max_hit_dice=10)
char2 = Character(name='arnold',max_hp=30,max_hit_dice=6)

def list_json_files(folder_path):
    json_files = [file[:-5] for file in os.listdir(folder_path) if file.endswith('.json')]
    return json_files

class FkGui4:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("v2")
        self.root.geometry("400x300")

        self.char = char1

        name_label = tk.Label(self.root, text=f"Name: {self.char.name}")
        name_label.grid(row=0, column=0)

        self.char1_button = tk.Button(self.root,text='Char1',
                                     command=self.char1_switch)
        self.char1_button.grid(row=1, column=0, pady=5)

        self.char2_button = tk.Button(self.root,text='Char2',
                                     command=self.char2_switch)
        self.char2_button.grid(row=1, column=1, pady=5)

    def char1_switch(self):
        self.char = char1
        name_label = tk.Label(self.root, text=f"Name: {self.char.name}")
        name_label.grid(row=0, column=0)


    def char2_switch(self):
        self.char = char2
        name_label = tk.Label(self.root, text=f"Name: {self.char.name}")
        name_label.grid(row=0, column=0)
        
    def run(self):
        self.root.mainloop()


if __name__ == '__main__': 
    gui = FkGui4()
    gui.run()
