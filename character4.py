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

    def damage(self,entry): 
        self.hp -= entry
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
        return all_stats
    
    def main_labels(self):
        return {'Hp':'hp',
                'Hit Dice': 'hit_dice',
                'AC':'AC', 
                'Save DC':'DC',
                'Attack':'atk',
                'Spell Attack':'sp_atk',
                'Initiative':'initiative',
                'Speed':'speed',
                'Prof. Bonus':'PB'}
                     