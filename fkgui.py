import tkinter as tk
import json,os
from character4 import Character


folder_path = 'save_files/'

def list_json_files(folder_path):
    json_files = [file[:-5] for file in os.listdir(folder_path) if file.endswith('.json')]
    return json_files

class FkGui4:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("400x300")
        self.auto_load_char()
        self._menu_setup()
        
    def live_buttons(self):
        def on_heal_button():
            if self.hp_entry.get().isdigit():
                entry = int(self.hp_entry.get())
                self.char.heal(entry=entry)
                self.update_frontpage()
            
        def on_damage_button():
            if self.hp_entry.get().isdigit():
                entry = int(self.hp_entry.get())
                self.char.damage(entry=entry)
                self.update_frontpage()

        def on_hit_dice_button():
            self.char.spend_hit_dice()
            self.update_frontpage()

        self.buttons_frame= tk.Frame(self.root)
        self.buttons_frame.grid(row=0,column=1,padx=10,sticky='w')
        #entry
       
        self.hp_entry = tk.Entry(self.buttons_frame,width=5)
        self.hp_entry.grid(row=0,column=0)
        
        #heal
        self.heal_button=tk.Button(self.buttons_frame,text='Heal',
                                   command=on_heal_button)
        self.heal_button.grid(row=0,column=1)
        #damage
        self.damage_button = tk.Button(self.buttons_frame,text='Damage',
                                     command=on_damage_button)
        self.damage_button.grid(row=0, column=2, pady=5)
        # hit dice
        self.hit_dice_button = tk.Button(self.buttons_frame,text='Hit Dice',
                                     command=on_hit_dice_button)
        self.hit_dice_button.grid(row=0, column=3, pady=5)



    def front_page(self):
        self.main_frame = tk.Frame(self.root)
        self.main_frame.grid(row=0,column=0,sticky='w')
        row_index = 0
        for label_name,attribute_name in self.char.main_labels().items():
            if label_name == 'Hp':
                label = tk.Label(self.main_frame, text=f"HP: {self.char.hp} / {self.char.max_hp}")
                label.grid(row=row_index,column=0,sticky='w')
                row_index += 1
            else:
                attribute = getattr(self.char,attribute_name)
                label = tk.Label(self.main_frame, text=f"{label_name}: {attribute}")
                label.grid(row=row_index,column=0,sticky='w')
                row_index += 1
        self.live_buttons()
       
    def _menu_setup(self):
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)
        # sub menus - filemenu
        self.character_files_menu()
        self.front_page()
        
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
        with open(file=folder_path+name+'.json') as file:
            stats = json.load(file)
        self.char = Character()
        for key,value in self.char.save_stats().items():
            setattr(self.char,value,stats[key])
        self.root.title(self.char.name)
        self.front_page()

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
                        setattr(self.char,key,int(value.get()))
                    except ValueError:
                        pass
                for key,value in other_widgets.items():
                    
                    try:
                        setattr(self.char,key,int(value.get()))
                    except ValueError:
                        pass

                self.char.hp = self.char.max_hp
                self.char.hit_dice = self.char.max_hit_dice
                self.save_char()
                self.update_frontpage()
                self.update_page.destroy()
            except ValueError:
                print('invalid entry')

        self.update_page = tk.Toplevel(self.root)
        self.update_page.title('Update Character')
        self.update_page.geometry('400x450')
        abilities_frame = tk.Frame(self.update_page)
        abilities_frame.grid(row=0,column=0,sticky='w')
        other_frame = tk.Frame(self.update_page)
        other_frame.grid(row=0,column=1,sticky='w')

        ability_widgets = {} 
        row_index = 0
        for text,attribute in self.char.ability_scores().items():
            label = tk.Label(abilities_frame, text=f'{text} {getattr(self.char,attribute)}')
            label.grid(row=row_index, column=0)
            entry = tk.Entry(abilities_frame, width=10)
            entry.grid(row=row_index, column=1)
            ability_widgets[attribute] = entry  # Store Entry widget in the dictionary
            row_index += 1
        
        other_widgets = {} 
        row_index = 0
        for text,attribute in self.char.other_stats().items():
            if text != 'Name':
                label = tk.Label(other_frame, text=f'{text} {getattr(self.char,attribute)}')
                label.grid(row=row_index, column=0)
                entry = tk.Entry(other_frame, width=10)
                entry.grid(row=row_index, column=1)
                other_widgets[attribute] = entry  # Store Entry widget in the dictionary
                row_index += 1
        

        done_button = tk.Button(self.update_page, text='Done', command=on_done_click)
        done_button.grid(row=row_index, column=1, pady=10)
        self.update_page.wait_window()

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
            
        self.creation_page = tk.Toplevel(self.root)
        self.creation_page.title('Character Creation')
        self.creation_page.geometry('400x450')
        abilities_frame = tk.Frame(self.creation_page)
        abilities_frame.grid(row=0,column=0,sticky='w')
        other_frame = tk.Frame(self.creation_page)
        other_frame.grid(row=0,column=1,sticky='w')

        self.char = Character()

        ability_widgets = {} 
        row_index = 0
        for text,attribute in self.char.ability_scores().items():
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
        done_button.grid(row=row_index, column=1, pady=10)
        self.creation_page.wait_window()

    def save_char(self):
        try:
            all_stats = {}
            for key,value in self.char.save_stats().items():
                stat=getattr(self.char,value)
                all_stats[key] = stat

            with open(folder_path+self.char.name+'.json','w') as file:
                json.dump(all_stats, file)
        
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
        self.root.title(self.char.name)
    
    def run(self):
        self.root.mainloop()
        self.save_char()

if __name__ == '__main__': 
    gui = FkGui4()
    gui.run()

