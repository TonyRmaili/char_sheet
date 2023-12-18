import tkinter as tk
from tkinter import filedialog  # Import filedialog separately
import json
from character4 import Character
folder_path = 'save_files/'
class LatestGui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("400x300")
        # Create a button for loading a file
        self.data =None
        self.load_button = tk.Button(self.root, text="Load File", command=self.load_file)
        self.load_button.pack(pady=10)

        self.save_bt = tk.Button(self.root, text="Save File", command=self.save_file)
        self.save_bt.pack(pady=10)

        self.new_bt = tk.Button(self.root, text="New File", command=self.new_file)
        self.new_bt.pack(pady=10)
           
   

    def load_file(self):
        file_path = filedialog.askopenfilename(initialdir=folder_path, title="Select a file", filetypes=[("JSON files", "*.json")])
        if file_path:
            with open(file_path, 'r') as file:
                self.data = json.load(file)
        
    def new_file(self):
        self.data = {'entered data':'value'}
        
              
    def update_file(self):
        self.data = {'new stuff':'best stuff'}


    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if file_path:
            with open(file_path, 'w') as file:
                json.dump(self.data, file)

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    gui = LatestGui()
    gui.run()
