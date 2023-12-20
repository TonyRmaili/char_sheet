import tkinter as tk
import json,os
from character5 import Character



folder_path = 'save_files5/'

def list_json_files(folder_path):
    json_files = [file[:-5] for file in os.listdir(folder_path) if file.endswith('.json')]
    return json_files

class NkGui5:
    def __init__(self):
        self.char =Character()
        self.root = tk.Tk()
        self.root.geometry("400x300")
        self.root_frame = tk.Frame(self.root)
        self.root_frame.pack()
        self.combat_entries_frame()
        self.combatframe()
        


    def combatframe(self):
        self.combat_frame = tk.LabelFrame(self.root_frame,text='Combat Stats')
        self.combat_frame.grid(row=0,column=1,padx=10,pady=10)
        self.combat_labels()
    
    def combat_entries_frame(self):
        self.combatentries_frame = tk.LabelFrame(self.root_frame,text='Combat Entries')
        self.combatentries_frame.grid(row=0,column=0,padx=10,pady=10)
        self.combat_entries()


    def combat_entries(self):
        def on_heal_button():
            if self.hp_entry.get().isdigit():
                entry = int(self.hp_entry.get())
                self.char.heal(entry=entry)
                
        def on_damage_button():
            if self.hp_entry.get().isdigit():
                entry = int(self.hp_entry.get())
                self.char.damage(entry=entry)
                self.update_frontpage()

        def on_hit_dice_button():
            self.char.spend_hit_dice()
            
        def on_temp_hp_button():
            
            if self.temp_hp_entry.get().isdigit():
                entry = int(self.temp_hp_entry.get())
                self.char.add_temp_hp(entry=entry)
                self.combat_frame.destroy()
                self.combatframe()


         # temp hp
        self.temp_hp_entry = tk.Entry(self.combatentries_frame,width=5)
        self.temp_hp_entry.grid(row=0,column=0)

        self.temp_hp_btn=tk.Button(self.combatentries_frame,text='Add Temp Hp',
                                   command=on_temp_hp_button)
        self.temp_hp_btn.grid(row=0,column=1)

        #entry
        self.hp_entry = tk.Entry(self.combatentries_frame,width=5)
        self.hp_entry.grid(row=1,column=0)
        #heal
        self.heal_button=tk.Button(self.combatentries_frame,text='Heal',
                                   command=on_heal_button)
        self.heal_button.grid(row=1,column=1)
        #damage
        self.damage_button = tk.Button(self.combatentries_frame,text='Damage',
                                     command=on_damage_button)
        self.damage_button.grid(row=1, column=2)
        # hit dice
        self.hit_dice_button = tk.Button(self.combatentries_frame,text='Hit Dice',
                                     command=on_hit_dice_button)
        self.hit_dice_button.grid(row=1, column=3)

        self.spell_book_button = tk.Button(self.combatentries_frame,text='Spell Book')
        self.spell_book_button.grid(row=2,column=0)

       

        for widget in self.combatentries_frame.winfo_children():
            widget.grid_configure(pady=5,sticky='news')




    def combat_labels(self):
        row_index = 0
        for label_name,attribute_name in self.char.combat_labels().items():
            if label_name == 'Hp':
                label = tk.Label(self.combat_frame,
                                  text=f"HP: {self.char.hp} / {self.char.max_hp}")
                label.grid(row=row_index,column=0,sticky='w')
                row_index += 1
            else:
                attribute = getattr(self.char,attribute_name)
                label = tk.Label(self.combat_frame, text=f"{label_name}: {attribute}")
                label.grid(row=row_index,column=0,sticky='w')
                row_index += 1

    def run(self):
        self.root.mainloop()
        

if __name__ == '__main__': 
    gui = NkGui5()
    gui.run()

