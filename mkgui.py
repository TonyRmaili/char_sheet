import tkinter as tk
import json,os
from character import Character

folder_path = 'save_files/'

def list_json_files(folder_path):
    json_files = [file[:-5] for file in os.listdir(folder_path) if file.endswith('.json')]
    return json_files

class MkGui3:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("v2")
        self.root.geometry("400x300")
        self.file_index = 0
        self.file_names = list_json_files(folder_path=folder_path)
        if not self.file_names:
            self.create_char_level()
            self.file_names = list_json_files(folder_path=folder_path)
        
        self.stats = self.load_character(self.file_names[self.file_index])
        
        # widgets
        self.menu_on_root= tk.Menu(self.root)
        self.load_char_menu()
        self.create_char_menu()
        self.root.config(menu=self.menu_on_root)

        name_label = tk.Label(self.root, text=f"Name: {self.char.name}")
        name_label.grid(row=1, column=0)
    
    def create_char_menu(self):
        menu = tk.Menu(self.menu_on_root, tearoff=0)
        menu.add_command(label='Create', command=self.create_char_level)
        self.menu_on_root.add_cascade(label='Create Character', menu=menu)

    def load_char_menu(self):
        self.menu_on_root.delete(2, tk.END)
        menu = tk.Menu(self.menu_on_root,tearoff=0)
        for file in self.file_names:
            menu.add_command(label=file,command=lambda name=file: self.load_character(name))
        self.menu_on_root.add_cascade(label='Load Character',menu=menu)
    
    def load_character(self,name):
        with open(file=folder_path+name+'.json') as file:
            self.stats = json.load(file)
                     
    def create_char_level(self):
        create_char_lvl = tk.Toplevel(self.root)
        create_char_lvl.title("Character Creation")
        create_char_lvl.geometry("300x400")

        stats = ['name', 'max_hp', 'max_hit_dice']
        entry_widgets = {} 

        def on_done_click():           
            stats = {stat: entry.get() for stat, entry in entry_widgets.items()}
            self.create_char_file(stats)
            create_char_lvl.destroy()

        row_index = 0
        for stat in stats:
            label = tk.Label(create_char_lvl, text=stat)
            label.grid(row=row_index, column=0)
            entry = tk.Entry(create_char_lvl, width=10)
            entry.grid(row=row_index, column=1)
            entry_widgets[stat] = entry  # Store Entry widget in the dictionary
            row_index += 1

        done_button = tk.Button(create_char_lvl, text='Done', command=on_done_click)
        done_button.grid(row=row_index, column=1, pady=10)
        create_char_lvl.wait_window()

    def create_char_file(self,stats):
        self.char = Character(name=stats['name'],max_hp=stats['max_hp'],max_hit_dice=stats['max_hit_dice'])
        
        with open(folder_path+stats['name']+'.json','w') as file:
            json.dump(stats, file)
        self.file_names = list_json_files(folder_path=folder_path)
        
    def run(self):
        self.root.mainloop()

if __name__ == '__main__': 
    gui = MkGui3()
    gui.run()