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

        # Dynamic label for current health and hit dice
        self.hp_label = tk.Label(self.root, text=f"Current HP: {self.char.hp}")
        self.hp_label.grid(row=2, column=3, pady=5, sticky='w')

        self.hit_dice_label = tk.Label(self.root, text=f"Current Hit Dice: {self.char.hit_dice}")
        self.hit_dice_label.grid(row=3, column=3, pady=5, sticky='w')
        self.hit_dice_button = tk.Button(self.root,text='Hit Dice',
                                     command=self.on_hit_dice_button)
        self.hit_dice_button.grid(row=0, column=4, pady=5)

        self.long_rest_button = tk.Button(self.root,text='Long Rest',
                                          command=self.take_long_rest)
        self.long_rest_button.grid(row=1, column=4, pady=5)

        # new windows - spells
        self.spell_book_button = tk.Button(self.root,text='Spell Book',
                                           command=self.open_spell_book)
        self.spell_book_button.grid(row=2, column=4, pady=5)

    def open_spell_book(self):
        spell_book_window = tk.Toplevel(self.root)
        spell_book_window.title("Spell Book")
        spell_book_window.geometry("300x200")

        dot_canvas = tk.Canvas(spell_book_window)
        dot_canvas.grid(row=0,column=1)
        dot_canvas.create_oval(10, 10, 100, 100, outline="black", fill="white")
        # lables- spells from character
        row_index = 0
        column_index = 0
        for spell in self.char.spells_prepered.keys():   
            spell_label = tk.Label(spell_book_window, text=spell)
            spell_label.grid(row=row_index,column=column_index)
            row_index += 1

    def take_long_rest(self):
        self.char.long_rest()
        self.update_hp_label()

    def on_hit_dice_button(self):
        self.char.spend_hit_dice()
        self.update_hp_label()

    def update_hp_label(self):
        self.hp_label.config(text=f"Current HP: {self.char.hp}")
        self.hit_dice_label.config(text=f'Current Hit Dice:{self.char.hit_dice}')

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
            self.char.max_hit_dice = stats.get('max_hit_dice',self.char.max_hit_dice)
            self.char.hit_dice = stats.get('hit_dice',self.char.hit_dice)
    
    def save_stats(self, filename='character_stats.json'):
        stats = {
            'hit_dice': self.char.hit_dice,
            'max_hit_dice':self.char.max_hit_dice,
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

