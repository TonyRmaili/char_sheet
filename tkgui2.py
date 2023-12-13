import tkinter as tk
import json,os
from character import Character

folder_path = 'save_files/'

def list_json_files(folder_path):
    json_files = [file[:-5] for file in os.listdir(folder_path) if file.endswith('.json')]
    return json_files

class TkGui2:
    def __init__(self,stats,char):
        self.root = tk.Tk()
        self.root.title("v2")
        self.root.geometry("400x300")
        self.char = char
        self.stats = stats

        # root menu
        self.menu_on_root= tk.Menu(self.root)
        self.load_char_menu()
        self.create_char_menu()
        self.root.config(menu=self.menu_on_root)


        self.heal_entry =tk.Entry(self.root,width=5)
        self.heal_entry.grid(row=0,column=0)
        self.heal_button=tk.Button(self.root,text='Heal'
                                   )
        self.heal_button.grid(row=0,column=1)

        name_label = tk.Label(self.root, text=f"Name: {self.char.name}")
        name_label.grid(row=1, column=0)

    def load_char_menu(self):
        menu = tk.Menu(self.menu_on_root,tearoff=0)
        self.file_names = list_json_files(folder_path=folder_path)
        for file in self.file_names:
            menu.add_command(label=file,command=lambda name=file: self.load_character(name))
        self.menu_on_root.add_cascade(label='Load Character',menu=menu)

    def load_character(self,name):
        self.char = Character(name=name)
        with open(file=folder_path+name+'.json') as file:
            stats = json.load(file)

            self.char.max_hp = stats.get('max_hp', self.char.max_hp)
            self.char.hp = stats.get('hp', self.char.hp)
            self.char.name = stats.get('name', self.char.name)
            self.char.max_hit_dice = stats.get('max_hit_dice',self.char.max_hit_dice)
            self.char.hit_dice = stats.get('hit_dice',self.char.hit_dice)
            for key, value in stats.items():
                print(f'{key}: {value}')

    def create_char_menu(self):
        menu = tk.Menu(self.menu_on_root, tearoff=0)
        menu.add_command(label='Create', command=self.create_char_level)
        self.menu_on_root.add_cascade(label='Create Character', menu=menu)

    def create_char_file(self,stats):  
        char = Character(name=stats['name'])
        stats = {
                'hit_dice': char.hit_dice,
                'max_hit_dice':char.max_hit_dice,
                'max_hp': char.max_hp,
                'hp': char.hp,
                'name': char.name
            }
        with open(folder_path+stats['name']+'.json','w') as file:
            json.dump(stats, file)
        return stats,char

    def create_char_level(self):
        create_char_lvl = tk.Toplevel(self.root)
        create_char_lvl.title("Character Creation")
        create_char_lvl.geometry("300x400")

        stats = ['name', 'max_hp', 'max_hit_dice']
        entry_widgets = {} 

        def on_done_click():           
            stats = {stat: entry.get() for stat, entry in entry_widgets.items()}
            self.create_char_file(stats)

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


    def run(self):
        self.root.mainloop()

def load_character2():
    no_name = 'no_name'
    try:
        file_names = list_json_files(folder_path=folder_path)
        char_name = file_names[0]
        char = Character(name=char_name)
        with open(file=folder_path+char_name+'.json') as file:
            stats = json.load(file)
        return stats,char
    except IndexError as e:
        return create_char_file2(no_name)

def create_char_file2(filename):
    char = Character(name=filename)
    stats = {
            'hit_dice': char.hit_dice,
            'max_hit_dice':char.max_hit_dice,
            'max_hp': char.max_hp,
            'hp': char.hp,
            'name': char.name
        }
    with open(folder_path+filename+'.json','w') as file:
        json.dump(stats, file)
    return stats,char


if __name__ == '__main__':
    # create_char_file2('arnold')
    char_stats= load_character2()
    gui = TkGui2(stats=char_stats[0],char=char_stats[1])
    gui.run()
    