import tkinter as tk
import json,os
from character import Character

folder_path = 'save_files/'

def list_json_files(folder_path):
    json_files = [file[:-5] for file in os.listdir(folder_path) if file.endswith('.json')]
    return json_files

class TkGui2:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("v2")
        self.root.geometry("400x300")
        # init character
        self.char = Character(max_hp=100,hp=50,name='Garry')

        # root menu
        self.menu_on_root= tk.Menu(self.root)
        self.load_char_menu()
        self.root.config(menu=self.menu_on_root)


    def load_char_menu(self):
        menu = tk.Menu(self.menu_on_root,tearoff=0)
        file_names = list_json_files(folder_path=folder_path)
        for file in file_names:
            menu.add_command(label=file,command=lambda name=file: self.load_character(name))
        self.menu_on_root.add_cascade(label='Load Character',menu=menu)

    def load_character(self,name):
        with open(file=folder_path+name+'.json') as file:
            stats = json.load(file) 
            self.char.max_hp = stats.get('max_hp', self.char.max_hp)
            self.char.hp = stats.get('hp', self.char.hp)
            self.char.name = stats.get('name', self.char.name)
            self.char.max_hit_dice = stats.get('max_hit_dice',self.char.max_hit_dice)
            self.char.hit_dice = stats.get('hit_dice',self.char.hit_dice)
            for key, value in stats.items():
                print(f'{key}: {value}')

            

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    gui = TkGui2()
    gui.run()
    