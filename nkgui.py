import tkinter as tk
from tkinter import ttk
import json,os
from character5 import Character


folder_path = 'save_files5/'

def list_json_files(folder_path):
    json_files = [file[:-5] for file in os.listdir(folder_path) if file.endswith('.json')]
    return json_files

class FkGui4:
    def __init__(self):
        self.root = tk.Tk()
        
        self.root_frame = tk.Frame(self.root)
        self.root_frame.pack()

        self.auto_load_char()
        self._menu_setup()
    
   
    def create_char_page(self):
        def on_done_click():
            try:
                for key,value in ability_widgets.items():
                    try:
                        setattr(self.char,key,int(value.get()))
                    except ValueError:
                        setattr(self.char,key,10)
                for key,value in other_widgets.items():
                    if value.get().isdigit():
                        setattr(self.char,key,int(value.get()))
                    else:
                        setattr(self.char,key,value.get())

                self.char.hp = self.char.max_hp
                self.char.hit_dice = self.char.max_hit_dice
                self.save_char()
                self.update_frontpage()
                self.creation_page.destroy()
            except ValueError:
                print('invalid entry')
            
        self.creation_page = tk.Toplevel(self.root_frame)
        self.creation_page.title('Character Creation')
       
        
        other_frame = tk.LabelFrame(self.creation_page,text='Other Stats')
        other_frame.grid(row=0,column=0,sticky='wsn')
        abilities_frame = tk.LabelFrame(self.creation_page,text='Ability Scores')
        abilities_frame.grid(row=0,column=1,sticky='wsn')

        self.char = Character()

        ability_widgets = {} 
        row_index = 0
        for text,attribute in self.char.ability_scores.items():
            label = tk.Label(abilities_frame, text=text)
            label.grid(row=row_index, column=0)
            entry = tk.Entry(abilities_frame, width=10)
            entry.grid(row=row_index, column=1)
            ability_widgets[attribute] = entry  # Store Entry widget in the dictionary
            row_index += 1
        
        other_widgets = {} 
        row_index = 0
        for text,attribute in self.char.other_stats().items():
            label = tk.Label(other_frame, text=text)
            label.grid(row=row_index, column=0)
            entry = tk.Entry(other_frame, width=10)
            entry.grid(row=row_index, column=1)
            other_widgets[attribute] = entry  # Store Entry widget in the dictionary
            row_index += 1

        done_button = tk.Button(self.creation_page, text='Done', command=on_done_click)
        done_button.grid(row=row_index, column=0, pady=10,sticky='news')
        self.creation_page.wait_window()

    def save_char(self):
        try:
            all_stats = {}
            for key,value in self.char.save_stats().items():
                stat=getattr(self.char,value)
                all_stats[key] = stat
            all_stats['Spells Known'] = self.char.spells_known
            all_stats['Spell Slots'] = self.char.spell_slots
            all_stats['Saving Throws'] = self.char.saving_throws
            all_stats['Skills'] = self.char.skills
            with open(folder_path+self.char.name+'.json','w') as file:
                json.dump(all_stats, file,indent=4)
            self.menu_bar.destroy()
            self._menu_setup()
            self.root.config(menu=self.menu_bar)
        except tk.TclError:
            pass
        except AttributeError:
            pass
        except TypeError:
            pass
    
    def auto_load_char(self):
        self.file_names = list_json_files(folder_path=folder_path)
        if self.file_names == []:
            self.create_char_page()
            self.file_names = list_json_files(folder_path=folder_path)
        file_index = 0
        with open(file=folder_path+self.file_names[file_index]+'.json') as file:
            stats = json.load(file)
        self.char = Character()
        for key,value in self.char.save_stats().items():
            setattr(self.char,value,stats[key])
        self.char.spells_known = stats['Spells Known'] 
        self.char.spell_slots = stats['Spell Slots']
        self.char.saving_throws=stats['Saving Throws'] 
        self.char.skills = stats['Skills'] 
        self.root.title(self.char.name)
    
    def addspells_frame(self):
        def addspell():
            self.char.addspell(addspellname_entry.get(),addspelltier_entry.get())
            self.spell_book_window.destroy()
            self.open_spell_book()
            

        frame = tk.LabelFrame(self.spell_book_window,text='Edit Spells and Slots')
        frame.grid(row=1,column=0,padx=10,sticky='news')
            # spells-  button
        addspell_btn= tk.Button(frame,text='Add Spell',
                                    command=addspell)
                                                               
        addspell_btn.grid(row=0,column=3,padx=10,sticky='w')
            # entry name and label
        spellname_label = tk.Label(frame,text='Spell Name')
        spellname_label.grid(row=0,column=0)
        addspellname_entry =tk.Entry(frame,width=15)
        addspellname_entry.grid(row=0,column=1)
        
            # tier entry 
        addspelltier_entry = ttk.Combobox(frame,width=5,
                                          values=list(self.char.spell_tiers.keys()))
                                         
        addspelltier_entry.grid(row=0,column=2)
       

        # slots - button
        def spells_slots():
            tiers = []
            for tier in self.char.spell_tiers.keys():
                if tier == 'cantrip':
                    pass
                else:
                    tiers.append(tier)
            return tiers

        def add_slots():
            self.char.add_spellslot(spellslot_tier.get(),int(slot_amount.get()))
            self.update_frontpage()

        slots_lb = tk.Label(frame,text='Spell Slots')
        slots_lb.grid(row=1,column=0)
        spellslot_tier= ttk.Combobox(frame,values=spells_slots(),width=5)
                                    
        spellslot_tier.grid(row=1,column=1,padx=10,sticky='w')

        slot_amount = tk.Spinbox(frame, from_=1, to='infinity',width=5)
        slot_amount.grid(row=1,column=2)

        add_slots_btn = tk.Button(frame,text='Add Slots',command=add_slots)
        add_slots_btn.grid(row=1,column=3)

    def spells_know_frame(self):
        frame = tk.LabelFrame(self.spell_book_window,text='Spells Known')
        frame.grid(row=0,column=0,padx=10,pady=10,sticky='wsn')
        row_index = 0
        for tier,name in self.char.spells_known.items():
            label = tk.Label(frame,text=f'{name} {tier}')
            label.grid(row=row_index,column=0,padx=5,pady=5,sticky='w')
            row_index +=1

    def open_spell_book(self):
            self.spell_book_window = tk.Toplevel(self.root)
            self.spell_book_window.title("Spell Book")
            self.spells_know_frame()
            self.addspells_frame()

    def open_details_page(self):
        self.details_page = tk.Toplevel(self.root)
        self.details_page.title("Character Details")

        ability_score_fr = tk.LabelFrame(self.details_page,text='Ability Scores')
        ability_score_fr.grid(row=0,column=0,padx=10,pady=10)

        saving_throws_fr = tk.LabelFrame(self.details_page,text='Saving Throws')
        saving_throws_fr.grid(row=0,column=1)

        skills_fr = tk.LabelFrame(self.details_page,text='Skills')
        skills_fr.grid(row=0,column=2)

        short_rest_skills_fr = tk.LabelFrame(self.details_page,text='Short Rest Skills')
        short_rest_skills_fr.grid(row=1,column=0)

        long_rest_skills_fr = tk.LabelFrame(self.details_page,text='Long Rest Skills')
        long_rest_skills_fr.grid(row=1,column=1)

        spells_know_fr = tk.LabelFrame(self.details_page,text='Spells Known')
        spells_know_fr.grid(row=2,column=0)

        def ability_scores():
            row_index = 0
            for text,attribute in self.char.ability_scores.items():
                label = tk.Label(ability_score_fr, text=f'{text} {getattr(self.char,attribute)}')
                label.grid(row=row_index, column=0)
                row_index += 1

        def saving_throws():
            pass

        def short_rest_skills():
            pass

        def long_rest_skills():
            pass

        def skills():
            pass

        ability_scores()

    def live_buttons(self):
        def on_heal_button():
            if self.hp_entry.get().isdigit():
                entry = int(self.hp_entry.get())
                self.char.heal(entry=entry)
                hp_lb.config(text=f'HP {self.char.hp}/{self.char.max_hp}')
            
        def on_damage_button():
            if self.hp_entry.get().isdigit():
                entry = int(self.hp_entry.get())
                self.char.damage(entry=entry)
                hp_lb.config(text=f'HP {self.char.hp}/{self.char.max_hp}')
                temp_hp_lb.config(text=f'Temp HP {self.char.temp_hp}')

        def on_hit_dice_button():
            self.char.spend_hit_dice()
            hit_dice_lb.config(text=f'Hit Dice {self.char.hit_dice}/{self.char.max_hit_dice}') 
            hp_lb.config(text=f'HP {self.char.hp}/{self.char.max_hp}')

        def on_temp_hp_button():
            if self.hp_entry.get().isdigit():
                entry = int(self.hp_entry.get())
                self.char.add_temp_hp(entry=entry)
                temp_hp_lb.config(text=f'Temp HP {self.char.temp_hp}')

        def take_short_rest():
            self.char.take_short_rest()
            hit_dice_lb.config(text=f'Hit Dice {self.char.hit_dice}/{self.char.max_hit_dice}') 

        def take_long_rest():
            self.char.take_long_rest()
            hit_dice_lb.config(text=f'Hit Dice {self.char.hit_dice}/{self.char.max_hit_dice}') 
            hp_lb.config(text=f'HP {self.char.hp}/{self.char.max_hp}')
            temp_hp_lb.config(text=f'Temp HP {self.char.temp_hp}')
            self.update_frontpage()

        self.buttons_frame= tk.LabelFrame(self.root_frame,text=f'Gameplay Box')
        self.buttons_frame.grid(row=0,column=1,padx=10,sticky='new')

        hp_lb = tk.Label(self.buttons_frame,text=f'HP {self.char.hp}/{self.char.max_hp}')
        temp_hp_lb =tk.Label(self.buttons_frame,text=f'Temp HP {self.char.temp_hp}')
        hit_dice_lb = tk.Label(self.buttons_frame,text=f'Hit Dice {self.char.hit_dice}/{self.char.max_hit_dice}')

        hp_lb.grid(row=0,column=0)
        temp_hp_lb.grid(row=0,column=1)
        hit_dice_lb.grid(row=0,column=2)

        details_btn=tk.Button(self.buttons_frame,text='Details',
                                   command=self.open_details_page)
        details_btn.grid(row=3,column=0)

        notes_btn=tk.Button(self.buttons_frame,text='Notes',
                                   command=self.open_details_page)
        notes_btn.grid(row=3,column=1)

        inv_btn=tk.Button(self.buttons_frame,text='Inventory',
                                   command=self.open_details_page)
        inv_btn.grid(row=3,column=2)

        pet_btn=tk.Button(self.buttons_frame,text='Pets',
                                   command=self.open_details_page)
        pet_btn.grid(row=3,column=3)
        
        #entry
        self.hp_entry = tk.Entry(self.buttons_frame,width=5)
        self.hp_entry.grid(row=1,column=0)
        #heal
        self.heal_button=tk.Button(self.buttons_frame,text='Heal',
                                   command=on_heal_button)
        self.heal_button.grid(row=1,column=1)
        #damage
        self.damage_button = tk.Button(self.buttons_frame,text='Damage',
                                     command=on_damage_button)
        self.damage_button.grid(row=1, column=2)
        # hit dice
        self.hit_dice_button = tk.Button(self.buttons_frame,text='Hit Dice',
                                     command=on_hit_dice_button)
        self.hit_dice_button.grid(row=2, column=3)

        self.spell_book_button = tk.Button(self.buttons_frame,text='Spell Book',command=self.open_spell_book)
        self.spell_book_button.grid(row=2,column=0)

        self.short_rest_btn = tk.Button(self.buttons_frame,text='Short Rest',command=take_short_rest)
        self.short_rest_btn.grid(row=2,column=1)

        self.long_rest_btn = tk.Button(self.buttons_frame,text='Long Rest',command=take_long_rest)
        self.long_rest_btn.grid(row=2,column=2)

        self.temp_hp_btn=tk.Button(self.buttons_frame,text='Add Temp Hp',
                                   command=on_temp_hp_button)
        self.temp_hp_btn.grid(row=1,column=3)

        for widget in self.buttons_frame.winfo_children():
            widget.grid_configure(sticky='news')

    def spells_frame(self):
        # slots frame
          
        self.spells_fr = tk.LabelFrame(self.root_frame,text='Spell Slots')
        self.spells_fr.grid(row=1,column=0,padx=10,pady=10,sticky='nsew')
        row_index = 0
        separator =0
        x, y, radius = 10, 10, 7
        for tier,slots in self.char.spell_slots.items():
            if slots['max'] ==0:
                pass
            else:
                frame = tk.LabelFrame(self.spells_fr,text=f'{tier}')
                frame.grid(row=row_index,column=0,sticky='news')
                # i = slots['current']
                canvas = tk.Canvas(frame,height=20,width=100)
                canvas.grid(row=row_index,column=0)
                
                for red_circle in range(slots['current']):
                    canvas.create_oval(x-radius+separator, y-radius,
                                        x+radius+separator, y+radius,outline='black',fill='red')
                    separator += 20
                for white_circle in range((slots['max']-slots['current'])):
                    canvas.create_oval(x-radius+separator, y-radius,
                                        x+radius+separator, y+radius,outline='black',fill='white')
                    separator += 20

                canvas.config(width=x+radius+separator+5)
                separator =0
                row_index +=1

       
        # manage slots frame
        def spells_slots():
            tiers = []
            for tier in self.char.spell_tiers.keys():
                if tier == 'cantrip':
                    pass
                else:
                    tiers.append(tier)
            return tiers
        
        def spend_slot():
            self.char.spend_slot(use_slot_entry.get())
            self.update_frontpage()

        def regain_slot():
            self.char.regain_slot(regain_slot_entry.get())
            self.update_frontpage()

        self.manage_slots_fr = tk.LabelFrame(self.root_frame,text='Manage Slots')
        self.manage_slots_fr.grid(row=1,column=1,padx=10,pady=10,sticky='nsew')

        use_slot_lb = tk.Label(self.manage_slots_fr,text='Spend Slot')
        use_slot_lb.grid(row=0,column=0)

        use_slot_entry = ttk.Combobox(self.manage_slots_fr,width=5,
                                          values=spells_slots())
        use_slot_entry.grid(row=1,column=0)

        use_slot_btn = tk.Button(self.manage_slots_fr,text='Cast'
                                  ,command=spend_slot)
        use_slot_btn.grid(row=2,column=0)
        
        regain_slot_lb = tk.Label(self.manage_slots_fr,text='Regain Slot')
        regain_slot_lb.grid(row=0,column=1)

        regain_slot_entry = ttk.Combobox(self.manage_slots_fr,width=5,
                                          values=spells_slots())
        regain_slot_entry.grid(row=1,column=1)

        regain_slot_btn = tk.Button(self.manage_slots_fr,text='Evocate'
                                    ,command=regain_slot)
        regain_slot_btn.grid(row=2,column=1)

    def front_page(self):
        self.main_frame = tk.LabelFrame(self.root_frame,text='Combat Stats')
        self.main_frame.grid(row=0,column=0,padx=10,pady=10,sticky='nsew')
        row_index = 0
        for label_name,attribute_name in self.char.combat_stats().items():    
            attribute = getattr(self.char,attribute_name)
            label = tk.Label(self.main_frame, text=f"{label_name}: {attribute}")
            label.grid(row=row_index,column=0)
            row_index += 1
        self.live_buttons()
        self.spells_frame()
        
    def _menu_setup(self):
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)
        # sub menus - filemenu
        self.character_files_menu()
       
        self.update_frontpage()
         
    def character_files_menu(self):
        self.char_menu = tk.Menu(self.menu_bar,font=('MV Boli',15),tearoff=0)
        self.char_menu.add_command(label='Create',command=self.create_char_page)
        self.char_menu.add_command(label='Save',command=self.save_char)
        self.char_menu.add_command(label='Update',command=self.update_char_page)
        self.menu_bar.add_cascade(label='Character',menu=self.char_menu)
        self.load_char_files_menu()
        
    def load_char_files_menu(self):
        self.file_names = list_json_files(folder_path=folder_path)
        self.load_chars = tk.Menu(self.char_menu,tearoff=0)
        for file_name in self.file_names:
            self.load_chars.add_command(label=file_name,command=lambda name=file_name: self.load_char(name))
        self.char_menu.add_cascade(label='Load',menu=self.load_chars)
        
    def load_char(self,name):
        self.save_char()
        with open(file=folder_path+name+'.json') as file:
            stats = json.load(file)
        self.char = Character()
        for key,value in self.char.save_stats().items():
            setattr(self.char,value,stats[key])
        self.char.spells_known = stats['Spells Known'] 
        self.char.spell_slots = stats['Spell Slots']
        self.char.saving_throws=stats['Saving Throws'] 
        self.char.skills = stats['Skills'] 
        self.root.title(self.char.name)
        self.update_frontpage()

    def update_frontpage(self):
        try:
            self.main_frame.destroy()
            self.buttons_frame.destroy()
        except AttributeError:
            pass
        self.root.title(self.char.name)
        self.front_page()

    def update_char_page(self):
        def on_done_click():
            try:
                for key,value in ability_widgets.items():
                    try:
                        setattr(self.char,key,int(value[0].get()))
                    except ValueError:
                        pass
                    self.char.saving_throws[key] = value[1].get()
   
                for key,value in other_widgets.items():
                    try:
                        setattr(self.char,key,int(value.get()))
                    except ValueError:
                        pass
                
                for key,value in skills_widget.items():
                    self.char.skills[key] = [value.get(),self.char.skills[key][1]]

                self.save_char()
                self.update_frontpage()
                self.update_page.destroy()
                
            except ValueError:
                print('invalid entry')

        self.update_page = tk.Toplevel(self.root)
        self.update_page.title('Update Character')
        abilities_frame = tk.LabelFrame(self.update_page,text='Ability Scores and Saving Throws')
        abilities_frame.grid(row=0,column=0,padx=10,pady=10,sticky='news')
        other_frame = tk.LabelFrame(self.update_page,text='Other Stats')
        other_frame.grid(row=0,column=1,sticky='nws',padx=10)
        skills_frame = tk.LabelFrame(self.update_page,text='Skills')
        skills_frame.grid(row=1,column=0,padx=10,pady=10,sticky='news')

        # ability scores
        ability_widgets = {} 
        row_index = 0
        for text,attribute in self.char.ability_scores.items():
            var = tk.BooleanVar(value=self.char.saving_throws[attribute])
            if var.get():
                label = tk.Label(abilities_frame,
                    text=f'{text} {getattr(self.char,attribute)} <{self.char.ability_mod(text)+self.char.PB}>')
            else:
                label = tk.Label(abilities_frame,
                    text=f'{text} {getattr(self.char,attribute)} <{self.char.ability_mod(text)}>')
            label.grid(row=row_index, column=0)
            entry = tk.Entry(abilities_frame, width=5)
            entry.grid(row=row_index, column=1)
            checkbox = tk.Checkbutton(abilities_frame,variable=var)
            checkbox.grid(row=row_index,column=2)
            ability_widgets[attribute] = (entry,var) # Store Entry widget in the dictionary
            row_index += 1
            
        # other stats - !change the label!
        other_widgets = {} 
        row_index = 0
        for text,attribute in self.char.other_stats().items():
            if text != 'Name':
                label = tk.Label(other_frame, text=f'{text} {getattr(self.char,attribute)}')
                label.grid(row=row_index, column=0)
                entry = tk.Entry(other_frame, width=5)
                entry.grid(row=row_index, column=1)
                other_widgets[attribute] = entry  # Store Entry widget in the dictionary
                row_index += 1
        
        # skills widgets
        row_index = 0
        skills_widget = {} 
        for name,prof in self.char.skills.items():
            var = tk.BooleanVar(value=self.char.skills[name][0])
            
            if var.get():
                label = tk.Label(skills_frame, text=f'{name} {self.char.ability_mod(prof[1])+self.char.PB}')
            else:
                label = tk.Label(skills_frame, text=f'{name} {self.char.ability_mod(prof[1])}')

            label.grid(row=row_index, column=0,sticky='w')
            checkbox = tk.Checkbutton(skills_frame,variable=var)
            checkbox.grid(row=row_index,column=1,sticky='w')
            skills_widget[name] = var
            row_index += 1

        done_button = tk.Button(self.update_page, text='Done', command=on_done_click)
        done_button.grid(row=row_index, column=1, pady=10,padx=10,sticky='news')
        self.update_page.wait_window()

    def run(self):
        self.root.mainloop()
        self.save_char()

if __name__ == '__main__': 
    gui = FkGui4()
    gui.run()

