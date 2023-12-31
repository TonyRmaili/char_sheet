import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
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
            all_stats['Feats and Traits']= self.char.feats_traits 
            all_stats['Notes'] = self.char.notes 
            all_stats['Inventory'] = self.char.inventory
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
        self.char.feats_traits = stats['Feats and Traits'] 
        self.char.notes = stats['Notes']
        self.char.inventory = stats['Inventory']
        self.root.title(self.char.name)

    def add_short_resets(self):
        def addskill():
            feat = {}
            if skillname_entry.get() == '':
                raise ValueError
            else:
                feat['name'] = skillname_entry.get()
              
            if skilltag_entry.get() == '':
                feat['tag'] = None
            else:
                feat['tag'] = skilltag_entry.get()

            if DC_type_entry.get() == '' or DC_entry.get() == '':
                feat['DC'] = None
            elif not DC_entry.get().isnumeric():
                raise ValueError
            else:
                feat['DC'] = {
                    'Type':DC_type_entry.get(),
                    'Value':DC_entry.get()
                }

            if text_widget.get("1.0", "end-1c") =='':
                feat['text'] = None
            else:
                feat['text'] = text_widget.get("1.0", "end-1c")

            if not var.get():
                feat['reset'] = None
                feat['charges'] = None
            else:
                feat['reset'] = rest_type_entry.get()
                feat['charges'] ={
                    'max' : charges.get(),
                    'current':charges.get()
                }
            self.char.feats_traits.append(feat)
            self.update_frontpage()
            print(self.char.feats_traits)
           
                    


        #topframe
        top_fr = tk.Frame(self.add_reset_frame)
        top_fr.pack()
        bottom_fr = tk.Frame(self.add_reset_frame)
        bottom_fr.pack()
        

        skillname_lb = tk.Label(top_fr,text='Skill Name')
        skillname_lb.grid(row=0,column=0)
        skillname_entry =tk.Entry(top_fr,width=15)
        skillname_entry.grid(row=0,column=1)

        skilltag_lb = tk.Label(top_fr,text='Skill Tag')
        skilltag_lb.grid(row=1,column=0)
        skilltag_entry =tk.Entry(top_fr,width=15)
        skilltag_entry.grid(row=1,column=1)
        
            # charges entry 
        var = tk.BooleanVar()
        charge_check_lb = tk.Label(top_fr,text='Has Charges?')
        charge_check_lb.grid(row=2,column=0)
        checkbox = tk.Checkbutton(top_fr,variable=var)
        checkbox.grid(row=2,column=1)

        charges_lb = tk.Label(top_fr,text='Charges')
        charges_lb.grid(row=3,column=0)                            
        charges = tk.Spinbox(top_fr, from_=1, to='infinity',width=5)
        charges.grid(row=3,column=1)

        
        DC_type_lb = tk.Label(top_fr,text='DC Type')
        DC_type_lb.grid(row=4,column=0)
        DC_type_entry = ttk.Combobox(top_fr,values=list(self.char.ability_scores.keys()),width=8) 
        DC_type_entry.grid(row=4,column=1) 

        DC_val_lb = tk.Label(top_fr,text='DC Value')
        DC_val_lb.grid(row=5,column=0)
        DC_entry =tk.Entry(top_fr,width=5)
        DC_entry.grid(row=5,column=1)

        rest_type_lb = tk.Label(top_fr,text='Rest Type')
        rest_type_lb.grid(row=6,column=0)
        rest_type_entry = ttk.Combobox(top_fr,values=['Short Rest','Long Rest'],width=10) 
        rest_type_entry.grid(row=6,column=1) 


        # bottom       
        info_lb =tk.Label(bottom_fr,text='Skill Info')
        info_lb.pack()
        addskill_btn= tk.Button(bottom_fr,text='Add Skill',
                                    command=addskill)
        addskill_btn.pack()
        text_widget = tk.Text(bottom_fr, wrap="word", height=5, width=20)
        text_widget.pack()
                                   
    def addspells_frame(self):
        def addspell():
            self.char.addspell(name=addspellname_entry.get(),
                               tier=addspelltier_entry.get(),
                               components=components.get(),
                               innate=innat_var.get(),
                               srange=range_box.get(),
                               duration= duration_box.get(),
                               action=action_box.get(),
                               concentration=con_var.get(),
                               text=text_widget.get("1.0", "end-1c"),
                               school=school_box.get()
                               )
    
            self.spell_book_window.destroy()
            self.open_spell_book()
            

        frame = tk.LabelFrame(self.spell_book_window,text='Edit Spells and Slots')
        frame.grid(row=1,column=0,padx=10,sticky='news')

        top_fr = tk.Frame(frame)
        top_fr.grid(row=0,column=0,sticky='w')
        bottom_fr = tk.Frame(frame)
        bottom_fr.grid(row=1,column=0,sticky='w',pady=5)

            # spells-  button
        addspell_btn= tk.Button(top_fr,text='Add Spell',
                                    command=addspell)
                                                               
        addspell_btn.grid(row=1,column=11,padx=10,sticky='w')
            # entry name and label
        spellname_label = tk.Label(top_fr,text='Spell Name')
        spellname_label.grid(row=0,column=0)
        addspellname_entry =tk.Entry(top_fr,width=15)
        addspellname_entry.grid(row=0,column=1)
        
            # tier entry 
        addspelltier_entry = ttk.Combobox(top_fr,width=5,
                                          values=list(self.char.spell_tiers.keys()))
                                         
        addspelltier_entry.grid(row=0,column=2)

        comp_list = ['V','S','M','VS','VM','SM','VSM']
        components = ttk.Combobox(top_fr,width=5,values=comp_list)
        components.grid(row=0,column=3)

        innate_lb = tk.Label(top_fr,text='Innate')
        innate_lb.grid(row=0,column=4)
        innat_var = tk.BooleanVar()
        innate_check = tk.Checkbutton(top_fr,variable=innat_var)
        innate_check.grid(row=0,column=5)

        # row 1
        school_list = ['Abjuration','Evocation','Transmutation',
                       'Conjuration','Divination','Necromany',
                       'Illusiob','Enchantment']
        school_box = ttk.Combobox(top_fr,values=school_list)
        school_box.grid(row=1,column=0)

        range_val = ['Touch','Self','Range','Special']
        range_box = ttk.Combobox(top_fr,width=5,values=range_val)
        range_box.grid(row=1,column=1)

        duration_val = ['Instantaneous','Rounds','Minutes','Hours','Days','Special']
        duration_box = ttk.Combobox(top_fr,width=5,values=duration_val)
        duration_box.grid(row=1,column=2)

        action_val = ['Action','Bonus Action','Reaction','Special']
        action_box = ttk.Combobox(top_fr,width=5,values=action_val)
        action_box.grid(row=1,column=3)

        concentration_lb = tk.Label(top_fr,text='Concentration')
        concentration_lb.grid(row=1,column=4)

        con_var = tk.BooleanVar()
        concentration_btn = tk.Checkbutton(top_fr,variable=con_var)
        concentration_btn.grid(row=1,column=5)

        for widget in top_fr.winfo_children():
            widget.grid_configure(sticky='w')

        text_widget = tk.Text(bottom_fr, wrap="word", height=5, width=45)
        text_widget.grid(row=0,column=0,sticky='news')

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

        slots_fr = tk.LabelFrame(bottom_fr,text='Spell Slots')
        slots_fr.grid(row=0,column=1,padx=10)

        spellslot_tier= ttk.Combobox(slots_fr,values=spells_slots(),width=5)                        
        spellslot_tier.grid(row=0,column=0,padx=10,sticky='w')

        slot_amount = tk.Spinbox(slots_fr, from_=1, to='infinity',width=5)
        slot_amount.grid(row=1,column=0)

        add_slots_btn = tk.Button(slots_fr,text='Add Slots',command=add_slots)
        add_slots_btn.grid(row=2,column=0)

        for widget in slots_fr.winfo_children():
            widget.grid_configure(pady=5)

    def spells_know_frame(self):
        frame = tk.Frame(self.spell_book_window)
        frame.grid(row=0,column=0,padx=10,pady=10,sticky='news')

        # info_frame = tk.Label(frame)
        # info_frame.grid(row=0,column=0)
        # max_preped_spells = tk.Label(info_frame,text=f'Max prepered Spells {self.char.max_prepered_spells}')
        # max_preped_spells.grid(row=0,column=0)
        # spell tier frames
        prepered_spells = []
        col_index = 0
        for tier,spells in self.char.spells_known.items():
            if spells == []:
                pass

            else:
                tier_frame = tk.LabelFrame(frame,text=f'{tier}')
                tier_frame.grid(row=1,column=col_index)
                col_index +=1
                for spell in enumerate(spells):
                    label = tk.Label(tier_frame,text=f'{spell[1]["name"]}')
                    label.grid(row=spell[0],column=0)
                    if tier != 'cantrip':
                        var = tk.IntVar()
                        check_btn = tk.Checkbutton(tier_frame,variable=var)
                        check_btn.grid(row=spell[0],column=1)

    def open_inventory_page(self):
        window = tk.Toplevel(self.root)
        window.title('Inventory')

        items_fr = tk.Frame(window)
        items_fr.grid(row=0,column=0,sticky='w')

        gold_fr = tk.LabelFrame(window,text='Manage Gold')
        gold_fr.grid(row=2,column=0,sticky='w')

        add_item_fr = tk.LabelFrame(window,text='Add Item')
        add_item_fr.grid(row=1,column=0,sticky='w')

        item_top_fr = tk.Frame(add_item_fr)
        item_top_fr.grid(row=0,column=0,sticky='w')
        item_bot_fr =tk.Frame(add_item_fr)
        item_bot_fr.grid(row=1,column=0)
        

        def items_frames():
            def open_item_info(i,item):
                item_window = tk.Toplevel(self.root)
                item_window.title(item["name"])
                top_fr = tk.Frame(item_window)
                top_fr.pack()
                bottom_fr = tk.Frame(item_window)
                bottom_fr.pack()

                def delete_item(i,item):    
                    self.char.inventory[item["type"]].pop(i)
                    self.save_char()
                    item_window.destroy()
                    window.destroy()
                
                for key,val in item.items():
                    if key != 'name':
                        label = tk.Label(top_fr,text=f'{key} : {val}')
                        label.pack(padx=5, pady=5)

                text_widget = scrolledtext.ScrolledText(bottom_fr, wrap=tk.WORD, width=40, height=10)
                text_widget.insert(tk.END, item['text'])
                text_widget.pack(padx=10, pady=10)

                delete_btn = tk.Button(item_window,text='Delete',command=lambda:delete_item(i,item))
                delete_btn.pack()

            row_index =0
            col_index=0
            for itype,pitems in self.char.inventory.items():
                if pitems == []:
                    pass
                else:
                    frame = tk.LabelFrame(items_fr,text=f'{itype}')
                    frame.grid(row=row_index,column=col_index,sticky='w')
                    col_index+=1
                    for i,item in enumerate(pitems):         
                        btn = tk.Button(frame,text=f'{item["name"]}',
                                        command=lambda i=i,item=item :open_item_info(i,item))
                        btn.grid(row=row_index,column=0,sticky='w')
                        row_index+=1
                row_index =0
                    

        def add_gold():
            try:
                self.char.gold += int(self.gold_entry.get())
            except ValueError:
                pass

        def spend_gold():
            try:
                self.char.gold -= int(self.gold_entry.get())
            except ValueError:
                pass
       
        def gold_widgets():
            self.gold_entry = tk.Entry(gold_fr,width=5)
            self.gold_entry.grid(row=0,column=0)
            add_btn = tk.Button(gold_fr,text='Add',
                                command=add_gold)
            add_btn.grid(row=0,column=1)
            spend_btn = tk.Button(gold_fr,text='Spend',
                                  command=spend_gold)
            spend_btn.grid(row=0,column=2)

        def add_item():
            name = item_name_entry.get()
            rarity = rarity_box.get()
            itype = type_box.get()
            if itype == '':
                itype = 'Other'
            attunement = attun.get()
            text = text_widget.get("1.0", "end-1c")

            item = {'name':name,'rarity':rarity,'type':itype,
                    'attunement':attunement,'text':text}
            if name =='':
                raise ValueError
            else:
                self.char.inventory[itype].append(item)
                self.save_char()

        item_name_lb = tk.Label(item_top_fr,text='Name')
        item_name_lb.grid(row=0,column=0,sticky='w')
        item_name_entry = tk.Entry(item_top_fr,width=8)
        item_name_entry.grid(row=0,column=1,sticky='w')

        rarities = ['Common','Uncommon','Rare','Very Rare','Legendary','Artifact']
        rarity_box = ttk.Combobox(item_top_fr,values=rarities,width=8)
        rarity_box.grid(row=0,column=2,sticky='w')

        types =['Tool','Armor','Weapon','Potion','Scroll','Ring',
                'Wondrous','Consumable','Other']
        type_box = ttk.Combobox(item_top_fr,values=types,width=9)
        type_box.grid(row=0,column=3,sticky='w')

        attun = tk.BooleanVar()
        attun_lb = tk.Label(item_top_fr,text='Attunment')
        attun_lb.grid(row=0,column=4,sticky='w')
        attunment_check = tk.Checkbutton(item_top_fr,variable=attun)
        attunment_check.grid(row=0,column=5)

        add_item_btn = tk.Button(item_top_fr,text='Pick up',
                                 command=add_item)
        add_item_btn.grid(row=0,column=6,sticky='w')


        text_widget = tk.Text(item_bot_fr, wrap="word", height=5, width=45)
        text_widget.pack()

        gold_widgets()
        items_frames()

    def open_spell_book(self):
            self.spell_book_window = tk.Toplevel(self.root)
            self.spell_book_window.title("Spell Book")
            self.spells_know_frame()
            self.addspells_frame()

    def open_notes_page(self):
        self.notes_page = tk.Toplevel(self.root)
        self.notes_page.title("Notes")
        notes_fr = tk.LabelFrame(self.notes_page,text='Notes')
        notes_fr.grid(row=0,column=0,sticky='w')
        add_note_fr = tk.LabelFrame(self.notes_page,text='Add Note')
        add_note_fr.grid(row=1,column=0,sticky='w')

        def add_note():
            title = title_entry.get()
            text = text_widget.get("1.0", "end-1c")
            self.char.notes.append({'title':title,'text':text})
            self.save_char()

        def open_note(title,text,i):
            note_window = tk.Toplevel(self.root)
            note_window.title(title)
            
            def delete_note(i):
                self.char.notes.pop(i)
                self.save_char()
                note_window.destroy()
                self.notes_page.destroy()

            text_widget = scrolledtext.ScrolledText(note_window, wrap=tk.WORD, width=40, height=10)
            text_widget.insert(tk.END, text)
            text_widget.pack(padx=10, pady=10)

            delete_btn = tk.Button(note_window,text='Delete',command=lambda:delete_note(i))
            delete_btn.pack()
            


        # add note 
        title_entry = tk.Entry(add_note_fr,width=40)
        title_entry.grid(row=0,column=1)
        add_btn = tk.Button(add_note_fr,text='Scribe',command=add_note)
        add_btn.grid(row=0,column=0)
        text_widget = tk.Text(add_note_fr, wrap="word", height=8, width=40)
        text_widget.grid(row=1,column=1)

        # loop on notes
        row_index =0
        col_index =0
        for i,note in enumerate(self.char.notes):
            if row_index%6 == 0:
                        col_index+=1
                        row_index = 0
            btn = tk.Button(notes_fr,text=f'{note["title"]}',
                            command=lambda title =note["title"],text=note["text"],index = i:open_note(title,text,index))
            btn.grid(row=row_index,column=col_index,sticky='w')
            row_index+=1
                  
    def open_details_page(self):
        self.details_page = tk.Toplevel(self.root)
        self.details_page.title("Character Details")

        ability_score_fr = tk.LabelFrame(self.details_page,text='Ability Scores')
        ability_score_fr.grid(row=0,column=0,sticky='nws')

        rest_skills_fr = tk.Frame(self.details_page)
        rest_skills_fr.grid(row=1,column=0,sticky='news')

        spells_know_fr = tk.LabelFrame(self.details_page,text='Spells Known')
        spells_know_fr.grid(row=2,column=0,sticky='news')
        # saving_throws_fr = tk.LabelFrame(self.details_page,text='Saving Throws')
        # saving_throws_fr.grid(row=0,column=0)

        # skills_fr = tk.LabelFrame(self.details_page,text='Skills')
        # skills_fr.grid(row=0,column=2)
    
        def spells_known():
            def open_spell_info(spell,tier,i):
                def delete_spell(i,tier):
                    self.char.spells_known[tier].pop(i)
                    spell_window.destroy()
                    self.details_page.destroy()
                    
                spell_window = tk.Toplevel(self.root)
                spell_window.title(spell['name'])

                quick_fr = tk.Frame(spell_window)
                quick_fr.pack()

                text_fr = tk.Frame(spell_window)
                text_fr.pack()

                row_i = 0
                for label,value in spell.items():
                    if label != 'text':
                        lb = tk.Label(quick_fr,text=f'{label}: {value}',
                                      font=('MV Boli',15))    
                        lb.grid(row=row_i,column=0,sticky='w',padx=20)
                        row_i+=1

                text_widget = scrolledtext.ScrolledText(text_fr, wrap=tk.WORD, width=40, height=10)
                text_widget.insert(tk.END, spell['text'])
                text_widget.pack(padx=10, pady=10)

                delete_btn = tk.Button(spell_window,text='Delete',command=lambda:delete_spell(i,tier))
                delete_btn.pack()

            col_index = 0
            for tier,spells in self.char.spells_known.items():
                if spells == []:
                    pass
                else:
                    tier_frame = tk.LabelFrame(spells_know_fr,text=f'{tier}')
                    tier_frame.grid(row=1,column=col_index)
                    col_index +=1
                    for spell in enumerate(spells):
                        btn = tk.Button(tier_frame,text=f'{spell[0]+1} {spell[1]["name"]}',
                                        command=lambda spell =spell[1],out_tier = tier,i=spell[0]: open_spell_info(spell,out_tier,i)) 
                        btn.grid(row=spell[0],column=0)
                        if tier != 'cantrip':
                            var = tk.IntVar()
                            check_btn = tk.Checkbutton(tier_frame,variable=var)
                            check_btn.grid(row=spell[0],column=1)

        def ability_scores():
            row_index = 0
            for text,attribute in self.char.ability_scores.items():
                label = tk.Label(ability_score_fr, text=f'{text} {getattr(self.char,attribute)}')
                label.grid(row=row_index, column=0)
                row_index += 1

        def saving_throws():
            pass

        def short_rest_skills():
            frame = tk.LabelFrame(rest_skills_fr,text='Short Skills')
            frame.grid(row=0,column=0,sticky='w')

            def open_skill_info(i,skill):
                def delete_skill(i):
                    self.char.feats_traits.pop(i)
                    skill_window.destroy()
                    self.details_page.destroy()
                    
                skill_window = tk.Toplevel(self.root)
                skill_window.title(skill['name'])

                quick_fr = tk.Frame(skill_window)
                quick_fr.pack()

                text_fr = tk.Frame(skill_window)
                text_fr.pack()

                row_i = 0
                for label,value in skill.items():
                    if label != 'text':
                        lb = tk.Label(quick_fr,text=f'{label}: {value}',
                                      font=('MV Boli',15))    
                        lb.grid(row=row_i,column=0,sticky='w',padx=20)
                        row_i+=1

                text_widget = scrolledtext.ScrolledText(text_fr, wrap=tk.WORD, width=40, height=10)
                text_widget.insert(tk.END, skill['text'])
                text_widget.pack(padx=10, pady=10)

                delete_btn = tk.Button(skill_window,text='Delete',command=lambda:delete_skill(i))
                delete_btn.pack()


            col_index = 0
            row_index = 0
            for i,skill in enumerate(self.char.feats_traits):
                if skill['reset'] == 'Short Rest':
                    if row_index%5 == 0:
                        col_index+=1
                        row_index = 0
                    btn = tk.Button(frame,text=f'{skill["name"]}',
                                    command=lambda index = i: open_skill_info(index,skill))
                    btn.grid(row=row_index,column=col_index,sticky='w')
                    row_index+=1
            
        def long_rest_skills():
            frame = tk.LabelFrame(rest_skills_fr,text='Long Skills')
            frame.grid(row=0,column=1,sticky='w')

            def open_skill_info(i,skill):
                def delete_skill(i):
                    self.char.feats_traits.pop(i)
                    skill_window.destroy()
                    self.details_page.destroy()
                    
                skill_window = tk.Toplevel(self.root)
                skill_window.title(skill['name'])

                quick_fr = tk.Frame(skill_window)
                quick_fr.pack()

                text_fr = tk.Frame(skill_window)
                text_fr.pack()

                row_i = 0
                for label,value in skill.items():
                    if label != 'text':
                        lb = tk.Label(quick_fr,text=f'{label}: {value}',
                                      font=('MV Boli',15))    
                        lb.grid(row=row_i,column=0,sticky='w',padx=20)
                        row_i+=1

                text_widget = scrolledtext.ScrolledText(text_fr, wrap=tk.WORD, width=40, height=10)
                text_widget.insert(tk.END, skill['text'])
                text_widget.pack(padx=10, pady=10)

                delete_btn = tk.Button(skill_window,text='Delete',command=lambda:delete_skill(i))
                delete_btn.pack()


            col_index = 0
            row_index = 0
            for i,skill in enumerate(self.char.feats_traits):
                if skill['reset'] == 'Long Rest':
                    if row_index%5 == 0:
                        col_index+=1
                        row_index = 0
                    btn = tk.Button(frame,text=f'{skill["name"]}',
                                    command=lambda index = i:open_skill_info(index,skill))
                    btn.grid(row=row_index,column=col_index,sticky='w')
                    row_index+=1

        def skills():
            pass

        ability_scores()
        short_rest_skills()
        long_rest_skills()
        spells_known()

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
                                   command=self.open_notes_page)
        notes_btn.grid(row=3,column=1)

        inv_btn=tk.Button(self.buttons_frame,text='Inventory',
                                   command=self.open_inventory_page)
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
        self.char.feats_traits = stats['Feats and Traits']  
        self.char.notes = stats['Notes']
        self.char.inventory = stats['Inventory']
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
        # add skills frames
        self.add_reset_frame = tk.LabelFrame(self.update_page,text='Feats and Traits')
        self.add_reset_frame.grid(row=1,column=1,padx=10,pady=10,sticky='news')
        
        
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
                label.grid(row=row_index, column=0,sticky='w')
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

        self.add_short_resets()
        
        done_button = tk.Button(self.update_page, text='Done', command=on_done_click)
        done_button.grid(row=row_index, column=1, pady=10,padx=10,sticky='news')
        self.update_page.wait_window()

    def run(self):
        self.root.mainloop()
        self.save_char()

if __name__ == '__main__': 
    gui = FkGui4()
    gui.run()

