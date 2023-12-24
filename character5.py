import math

class Character:
    def __init__(self,name=None,max_hp=None,max_hit_dice=None):
        self.name = name
        self.max_hp = max_hp
        self.max_hit_dice = max_hit_dice
        self.inspiration = 0
        # # ability score - int values
        self.stre= 0
        self.dex = 0
        self.con = 0
        self.inte = 0
        self.wis = 0
        self.cha= 0

        self.temp_hp = 0
        self.hp = self.max_hp
        self.hit_dice = self.max_hit_dice
        self.lvl=1
        self.PB = 0
        self.AC = 0
        self.initiative = 0
        self.speed = 0
        self.atk =0
        self.sp_atk= 0
        self.DC =0
        self.max_prepered_spells = 2
        self.reaction = True
        self.short_rest_abilities =[]
        self.long_rest_abilities=[]
        self.gold = 0
        self.spells_known = {}
        self.spells_prepared = {}
        self.spell_tiers = {'cantrip':0,'tier1':1,
                            'tier2':2,'tier3':3,
                            'tier4':4,'tier5':5,
                            'tier6':6,'tier7':7,
                            'tier8':8,'tier9':9}
        
        self.spell_slots = {'tier1':{'max':0,'current':0},
                            'tier2':{'max':0,'current':0},
                            'tier3':{'max':0,'current':0},
                            'tier4':{'max':0,'current':0},
                            'tier5':{'max':0,'current':0},
                            'tier6':{'max':0,'current':0},
                            'tier7':{'max':0,'current':0},
                            'tier8':{'max':0,'current':0},
                            'tier9':{'max':0,'current':0}
                            }
        
        self.saving_throws = {
                'stre':False,
                'dex':False,
                'con':False,
                'inte':False,
                'wis':False,
                'cha':False}
        
        self.skills = {'Acrobatics': False,
                        'Animal Handling': False,
                        'Arcana': False,
                        'Athletics': False,
                        'Deception': False,
                        'History': False,
                        'Insight': False,
                        'Intimidation': False,
                        'Investigation': False,
                        'Medicine': False,
                        'Nature': False,
                        'Perception': False,
                        'Performance': False,
                        'Persuasion': False,
                        'Religion': False,
                        'Sleight of Hand': False,
                        'Stealth': False, 
                        'Survival': False}
        
    def ability_mod(self):
        abs_mod = []
        for attribute in self.ability_scores().values():
            mod = getattr(self,attribute)
            if mod >= 10:
                mod = int((mod-10)/2)
                abs_mod.append(mod)        
            elif mod < 10:
                mod = int((mod-10)/2 -0.5)
                abs_mod.append(mod)
        return abs_mod
        
        
    
    def spend_slot(self,tier):
        self.spell_slots[tier]['current'] -=1
        if self.spell_slots[tier]['current'] <= 0:
            self.spell_slots[tier]['current'] = 0
        
    def regain_slot(self,tier):
        self.spell_slots[tier]['current'] +=1
        if self.spell_slots[tier]['current'] > self.spell_slots[tier]['max']:
            self.spell_slots[tier]['current'] = self.spell_slots[tier]['max']

    def add_spellslot(self,slot,amount):
        self.spell_slots[slot]['max'] += amount
        print(self.spell_slots)

    def take_short_rest(self):
        print('taking short rest')

    def take_long_rest(self):
        self.hp = self.max_hp
        self.temp_hp = 0
        self.hit_dice += math.ceil(self.max_hit_dice / 2)
        if self.hit_dice > self.max_hit_dice:
            self.hit_dice = self.max_hit_dice

        for tier in self.spell_slots.values():
            tier['current'] = tier['max']

    def addspell(self,name,tier):
        self.spells_known[tier] = name

    # not correct atm
    def damage(self,entry): 
        dmg_diff = self.temp_hp - entry
        if dmg_diff < 0:
            self.temp_hp = 0
            self.hp += dmg_diff
        else:
            self.temp_hp -= entry

        if self.hp < 0:
            self.hp = 0
        
    def heal(self,entry):
        heal = entry
        self.hp += heal
        if self.hp > self.max_hp:
            self.hp = self.max_hp
    
    def spend_hit_dice(self):
        self.hit_dice -= 1
        if self.hit_dice < 0:
            self.hit_dice = 0
            return 'no more hit dice left'
        self.heal(5)

    def add_temp_hp(self,entry):
        self.temp_hp += entry

    def live_buttons_tag(self):
        return {'Gold':'gold',
                'Hp':'hp',
                'Hit Dice': 'hit_dice'}

    def ability_scores(self):
        return {'Strength':'stre',
                'Dexterity':'dex',
                'Constitution':'con',
                'Inteligence':'inte',
                'Wisdom':'wis',
                'Charisma':'cha'}
    
    def other_stats(self):
        return {
            'Name':'name',
            'Max Hp':'max_hp',
            'Max Hit Dice':'max_hit_dice',
            'Total level':'lvl',
            'Prof. Bonus':'PB', 
            'AC':'AC', 
            'Initiative':'initiative', 
            'Speed':'speed', 
            'Attack':'atk', 
            'Spell Attack':'sp_atk',
            'Save DC':'DC', 
            'Max spells prepared':'max_prepered_spells',
            'Inspiration':'inspiration'
        }
    
    def save_stats(self):
        all_stats = {**self.other_stats(),**self.ability_scores()}
        all_stats['Hp'] = 'hp'
        all_stats['Hit Dice'] = 'hit_dice'
        all_stats['Temp Hp'] = 'temp_hp'
        return all_stats
   
    def combat_stats(self):
        return {'AC':'AC', 
                'Save DC':'DC',
                'Attack':'atk',
                'Spell Attack':'sp_atk',
                'Initiative':'initiative',
                'Speed':'speed' }

