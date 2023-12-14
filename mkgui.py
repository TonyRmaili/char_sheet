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
        self.root.geometry("400x300")
        self.file_index = 0
        self.file_names = list_json_files(folder_path=folder_path)
        if not self.file_names:
            self.create_char_level()
            self.file_names = list_json_files(folder_path=folder_path)  
        self.load_character(self.file_names[self.file_index])
        # widgets
        self.menu_on_root= tk.Menu(self.root)
        self.load_char_menu()
        self.create_char_menu()
        self.root.config(menu=self.menu_on_root)
        self.main_labels()
        self.buttons_with_entry()
        

    def main_labels(self):
        self.main_frame = tk.Frame(self.root)
        self.main_frame.grid(row=0,column=0,sticky='we')

        # row 0
        self.hp_label = tk.Label(self.main_frame, text=f"HP: {self.char.hp} / {self.char.max_hp}")
        self.hp_label.grid(row=0, column=0,padx=10)

        self.hit_dice = tk.Label(self.main_frame, text=f"Hit Dice: {self.char.hit_dice}")
        self.hit_dice.grid(row=0, column=1)

        self.AC_label = tk.Label(self.main_frame, text=f"AC: {self.char.AC}")
        self.AC_label.grid(row=0, column=2)

        self.DC_label = tk.Label(self.main_frame, text=f"DC: {self.char.DC}")
        self.DC_label.grid(row=0, column=3)

        self.atk_label = tk.Label(self.main_frame, text=f"Atk: +{self.char.atk}")
        self.atk_label.grid(row=0, column=4)

        self.ini_label = tk.Label(self.main_frame, text=f"Init: +{self.char.initiative}")
        self.ini_label.grid(row=0, column=5)

        # row 1
        self.speed_label = tk.Label(self.main_frame, text=f"Speed: {self.char.speed}")
        self.speed_label.grid(row=1, column=0)

        self.sp_atk_label = tk.Label(self.main_frame, text=f"Sp_atk: {self.char.sp_atk}")
        self.sp_atk_label.grid(row=1, column=1)

        self.PB_label = tk.Label(self.main_frame, text=f"PB: {self.char.PB}")
        self.PB_label.grid(row=1, column=2)

    def config_lables(self):
        try:
            self.hp_label.config(text=f"HP: {self.char.hp} / {self.char.max_hp}")
            self.hit_dice.config(text=f"Hit Dice: {self.char.hit_dice}")
            self.AC_label.config(text=f"AC: {self.char.AC}")
            self.DC_label.config(text=f"DC: {self.char.DC}")
            self.atk_label.config(text=f"Atk: {self.char.atk}")
            self.ini_label.config(text=f"Init: {self.char.initiative}")
            self.speed_label.config(text=f"Speed: {self.char.speed}")
            self.sp_atk_label.config(text=f"Sp_atk: {self.char.sp_atk}")
            self.PB_label.config(text=f'PB: {self.char.PB}')

        except AttributeError:
            pass


    def buttons_with_entry(self):
        def on_heal_button():
            self.char.heal(entry=self.heal_entry)
            self.config_lables()
        def on_damage_button():
            self.char.damage(entry=self.damage_entry)
            self.config_lables()
        def on_hit_dice_button():
            self.char.spend_hit_dice()
            self.config_lables()
        
        self.bwe_frame = tk.Frame(self.root)
        self.bwe_frame.grid(row=1,column=0,padx=5,pady=5)

        #heal
        self.heal_entry =tk.Entry(self.bwe_frame,width=5)
        self.heal_entry.grid(row=0,column=0)
        self.heal_button=tk.Button(self.bwe_frame,text='Heal',
                                   command=on_heal_button)
        self.heal_button.grid(row=0,column=1)
        #damge 
        self.damage_entry = tk.Entry(self.bwe_frame,width=5)
        self.damage_entry.grid(row=1, column=0, pady=5)
        self.damage_button = tk.Button(self.bwe_frame,text='Damage',
                                     command=on_damage_button)
        self.damage_button.grid(row=1, column=1, pady=5)

        # hit dice
        self.hit_dice_entry = tk.Entry(self.bwe_frame,width=5)
        self.hit_dice_entry.grid(row=2, column=0, pady=5)
        self.hit_dice_button = tk.Button(self.bwe_frame,text='Hit Dice',
                                     command=on_hit_dice_button)
        self.hit_dice_button.grid(row=2, column=1, pady=5)
    
    def buttons(self):
        self.buttons_frame= tk.Frame(self.root)
        self.buttons_frame.grid(row=0,column=2,padx=5,pady=5)

        self.spell_book_button = tk.Button(self.buttons_frame,text='Spell Book',
                                           command=self.open_spell_book)
        self.spell_book_button.grid(row=0, column=0, pady=5)

        self.long_rest_button = tk.Button(self.buttons_frame,text='Long Rest',
                                          command=self.take_long_rest)
        self.long_rest_button.grid(row=1, column=0, pady=5)

    

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
        self.char = Character(name=self.stats['name'],max_hp=self.stats['max_hp'],max_hit_dice=self.stats['max_hit_dice'])
        self.root.title(self.char.name)
        self.config_lables()
        
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
        self.root.title(self.char.name)
        self.config_lables()
        with open(folder_path+stats['name']+'.json','w') as file:
            json.dump(stats, file)
        self.file_names = list_json_files(folder_path=folder_path)
            
    def run(self):
        self.root.mainloop()

if __name__ == '__main__': 
    gui = MkGui3()
    gui.run()

