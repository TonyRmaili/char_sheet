import tkinter as tk
import json
from character import Character

class TkGui2:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Character Sheet")
        self.root.geometry("400x300")
        self.char = Character(max_hp=100,hp=50,name='Garry')

        self.main_labels()
        self.buttons_with_entry() 
        self.buttons()
        

    def buttons_with_entry(self):
        self.bwe_frame = tk.Frame(self.root,bg='green')
        self.bwe_frame.grid(row=1,column=0,padx=5,pady=5)

        #heal
        self.heal_entry =tk.Entry(self.bwe_frame)
        self.heal_entry.grid(row=0,column=0)
        self.heal_button=tk.Button(self.bwe_frame,text='Heal',
                                   command=self.on_heal_button)
        self.heal_button.grid(row=0,column=1)
        #damge 
        self.damage_entry = tk.Entry(self.bwe_frame)
        self.damage_entry.grid(row=1, column=0, pady=5)
        self.damage_button = tk.Button(self.bwe_frame,text='Damage',
                                     command=self.on_damage_button)
        self.damage_button.grid(row=1, column=1, pady=5)

        # hit dice
        self.hit_dice_entry = tk.Entry(self.bwe_frame)
        self.hit_dice_entry.grid(row=2, column=0, pady=5)
        self.hit_dice_button = tk.Button(self.bwe_frame,text='Hit Dice',
                                     command=self.on_hit_dice_button)
        self.hit_dice_button.grid(row=2, column=1, pady=5)
        
    def main_labels(self):
        self.main_frame = tk.Frame(self.root,bg='red')
        self.main_frame.grid(row=0,column=0,padx=5,pady=5)

        name_label = tk.Label(self.main_frame, text=f"Name: {self.char.name}")
        name_label.grid(row=0, column=0, pady=5, sticky='w')

        max_hp_label = tk.Label(self.main_frame, text=f"Max HP: {self.char.max_hp}")
        max_hp_label.grid(row=0, column=1, pady=5, sticky='w')

        self.hp_label = tk.Label(self.main_frame, text=f"Current HP: {self.char.hp}")
        self.hp_label.grid(row=0, column=2, pady=5, sticky='w')

        self.hit_dice_label = tk.Label(self.main_frame, text=f"Hit Dice: {self.char.hit_dice}")
        self.hit_dice_label.grid(row=0, column=3, pady=5, sticky='w')
    
    def buttons(self):
        self.buttons_frame= tk.Frame(self.root,bg='blue')
        self.buttons_frame.grid(row=1,column=1,padx=5,pady=5)


        self.spell_book_button = tk.Button(self.buttons_frame,text='Spell Book',
                                           command=self.open_spell_book)
        self.spell_book_button.grid(row=0, column=0, pady=5)

        self.long_rest_button = tk.Button(self.buttons_frame,text='Long Rest',
                                          command=self.take_long_rest)
        self.long_rest_button.grid(row=1, column=0, pady=5)


    def take_long_rest(self):
        pass
    
    def open_spell_book(self):
        print('sp open')

    def on_heal_button(self):
        print('+1')

    def on_damage_button(self):
        print('-1')
    def on_hit_dice_button(self):
        print('HD spent')
    
    def run(self):       
        self.root.mainloop()


if __name__=='__main__':
    gui = TkGui2()
    gui.run()
