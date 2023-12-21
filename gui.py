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

        self.main_labels()
        self.buttons_with_entry() 
        self.buttons()
        self.new_char_menu()

    def new_char_menu(self):
        self.new_char = tk.Menu(self.root,tearoff=0)
        self.new_char.add_command(label='New Character',command=self.create_char_window)
        self.root.config(menu=self.new_char)

    def side_character(self):
        pass

    def create_char(self):
        print('done')

    def create_char_window(self):
        window=tk.Toplevel(self.root)
        window.title('Character Creation')
        window.geometry('300x400')

        self.done = tk.Menu(window,tearoff=0)
        self.done.add_command(label='Done',command=self.create_char)
        window.config(menu=self.done)

        # frame for attributes
        attributes_frame = tk.Frame(window)
        attributes_frame.grid(row=0,column=0)
        # frame for other stuff
        other_frame = tk.Frame(window)
        other_frame.grid(row=0,column=1)

        name_label = tk.Label(other_frame,text=f'Name:')
        name_label.grid(row=0,column=0)
        name_entry = tk.Entry(other_frame,width=15)
        name_entry.grid(row=0,column=1)

        max_hp_label = tk.Label(other_frame,text=f'Max Hp:')
        max_hp_label.grid(row=1,column=0)
        max_hp_entry = tk.Entry(other_frame,width=5)
        max_hp_entry.grid(row=1,column=1)
        

        # ability scores
        stre_label = tk.Label(attributes_frame,text=f'Strenght:')
        stre_label.grid(row=0,column=0)
        stre_entry = tk.Entry(attributes_frame,width=5)
        stre_entry.grid(row=0,column=1)

        dex_label = tk.Label(attributes_frame,text=f'Dexterity:')
        dex_label.grid(row=1,column=0)
        dex_entry = tk.Entry(attributes_frame,width=5)
        dex_entry.grid(row=1,column=1)
        
        con_label = tk.Label(attributes_frame,text=f'Constitution:')
        con_label.grid(row=2,column=0)
        con_entry = tk.Entry(attributes_frame,width=5)
        con_entry.grid(row=2,column=1)
        
        inte_label = tk.Label(attributes_frame,text=f'Intelligence:')
        inte_label.grid(row=3,column=0)
        inte_entry = tk.Entry(attributes_frame,width=5)
        inte_entry.grid(row=3,column=1)

        wis_label = tk.Label(attributes_frame,text=f'Wisdom:')
        wis_label.grid(row=4,column=0)
        wis_entry = tk.Entry(attributes_frame,width=5)
        wis_entry.grid(row=4,column=1)

        cha_label = tk.Label(attributes_frame,text=f'Charisma:')
        cha_label.grid(row=5,column=0)
        cha_entry = tk.Entry(attributes_frame,width=5)
        cha_entry.grid(row=5,column=1)

    def buttons_with_entry(self):
        self.bwe_frame = tk.Frame(self.root)
        self.bwe_frame.grid(row=0,column=1,padx=5,pady=5)

        #heal
        self.heal_entry =tk.Entry(self.bwe_frame,width=5)
        self.heal_entry.grid(row=0,column=0)
        self.heal_button=tk.Button(self.bwe_frame,text='Heal',
                                   command=self.on_heal_button)
        self.heal_button.grid(row=0,column=1)
        #damge 
        self.damage_entry = tk.Entry(self.bwe_frame,width=5)
        self.damage_entry.grid(row=1, column=0, pady=5)
        self.damage_button = tk.Button(self.bwe_frame,text='Damage',
                                     command=self.on_damage_button)
        self.damage_button.grid(row=1, column=1, pady=5)

        # hit dice
        self.hit_dice_entry = tk.Entry(self.bwe_frame,width=5)
        self.hit_dice_entry.grid(row=2, column=0, pady=5)
        self.hit_dice_button = tk.Button(self.bwe_frame,text='Hit Dice',
                                     command=self.on_hit_dice_button)
        self.hit_dice_button.grid(row=2, column=1, pady=5)
        
    def main_labels(self):
        self.main_frame = tk.Frame(self.root)
        self.main_frame.grid(row=0,column=0)

        name_label = tk.Label(self.main_frame, text=f"Name: {self.char.name}")
        name_label.grid(row=0, column=0)

        max_hp_label = tk.Label(self.main_frame, text=f"Max HP: {self.char.max_hp}")
        max_hp_label.grid(row=1, column=0)

        self.hp_label = tk.Label(self.main_frame, text=f"Current HP: {self.char.hp}")
        self.hp_label.grid(row=2, column=0)

        self.hit_dice_label = tk.Label(self.main_frame, text=f"Hit Dice: {self.char.hit_dice}")
        self.hit_dice_label.grid(row=3, column=0)
    
    def buttons(self):
        self.buttons_frame= tk.Frame(self.root)
        self.buttons_frame.grid(row=0,column=2,padx=5,pady=5)


        self.spell_book_button = tk.Button(self.buttons_frame,text='Spell Book',
                                           command=self.open_spell_book)
        self.spell_book_button.grid(row=0, column=0, pady=5)

        self.long_rest_button = tk.Button(self.buttons_frame,text='Long Rest',
                                          command=self.take_long_rest)
        self.long_rest_button.grid(row=1, column=0, pady=5)

    def open_spell_book(self):
        spell_book_window = tk.Toplevel(self.root)
        spell_book_window.title("Spell Book")
        spell_book_window.geometry("300x200")

        # lables- spells from character
        row_index = 0
        for spell in self.char.spells_prepered.keys():   
            spell_label = tk.Label(spell_book_window, text=spell)
            spell_label.grid(row=row_index,column=0)
            checkbutton = tk.Checkbutton(spell_book_window)
            checkbutton.grid(row=row_index,column=1,pady=5)
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

