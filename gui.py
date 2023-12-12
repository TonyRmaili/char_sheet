import tkinter as tk
import json
from character import Character

class TkGui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Character Sheet")
        self.root.geometry("400x300")
        
        self.char = Character(max_hp=100,hp=50,name='Garry')
        self.load_stats()
        # heal
        self.heal_entry = tk.Entry(self.root)
        self.heal_entry.grid(row=0, column=0, pady=5)
        self.heal_button = tk.Button(self.root,text='Heal',
                                     command=self.on_heal_button)
        self.heal_button.grid(row=0, column=1, pady=5)

        # damage
        self.damage_entry = tk.Entry(self.root)
        self.damage_entry.grid(row=1, column=0, pady=5)
        self.damage_button = tk.Button(self.root,text='Damage',
                                     command=self.on_damage_button)
        self.damage_button.grid(row=1, column=1, pady=5)

        # labels
        name_label = tk.Label(self.root, text=f"Name: {self.char.name}")
        name_label.grid(row=0, column=3, pady=5, sticky='w')

        max_hp_label = tk.Label(self.root, text=f"Max HP: {self.char.max_hp}")
        max_hp_label.grid(row=1, column=3, pady=5, sticky='w')

        # Dynamic label for current health
        self.hp_label = tk.Label(self.root, text=f"Current HP: {self.char.hp}")
        self.hp_label.grid(row=2, column=3, pady=5, sticky='w')

    def update_hp_label(self):
        self.hp_label.config(text=f"Current HP: {self.char.hp}")

    def on_heal_button(self):
        self.char.heal(entry=self.heal_entry)
        self.update_hp_label()

    def on_damage_button(self):
        self.char.damage(entry=self.damage_entry)
        self.update_hp_label()

    def load_stats(self,filename='character_stats.json'):
        with open(filename) as file:
            stats= json.load(file)
            self.char.max_hp = stats.get('max_hp', self.char.max_hp)
            self.char.hp = stats.get('hp', self.char.hp)
            self.char.name = stats.get('name', self.char.name)
    
    def save_stats(self, filename='character_stats.json'):
        stats = {
            'max_hp': self.char.max_hp,
            'hp': self.char.hp,
            'name': self.char.name
        }
        with open(filename, 'w') as file:
            json.dump(stats, file)
    

    def run(self):
        
        self.root.mainloop()
        self.save_stats()

if __name__=='__main__':
    gui = TkGui()
    gui.run()

