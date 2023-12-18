
class Character:
    def __init__(self,name='name',max_hp=1,max_hit_dice=1):
        self.name = name
        self.max_hp = max_hp
        self.max_hit_dice = max_hit_dice
        self.inspiration = 0
        # ability score - int values
        self.stre=0
        self.dex = 0
        self.con = 3
        self.inte = 0
        self.wis =0
        self.cha=0
        self.abilities2 = {'Strenght':'stre',
                          'Dexterity':'dex',
                          'Constitution':'con',
                          'Inteligence':'inte',
                          'Wisdom':'wis',
                          'Charisma':'cha'}
                   
        # main labels - int values
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
        self.other_stats2 = {
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

        self.main_labels = {'HP':'hp','Hit Dice':'hit_dice'}
        self.spells_prepered = {
                                'Eldritch Blast':'cantrip',
                                'Armor of Aghatys': 'tier 1',
                                'Invisibility': 'tier 2'}
        
        
        self.reaction = True
        self.short_rest_abilities =[]
        self.long_rest_abilities=[]
        self.setup_spell_tiers()
       
    def merge_all_stats(self):
        merged_stats = {**self.other_stats2,
                         **self.abilities2,**self.main_labels}
        return merged_stats

    def setup_spell_tiers(self):
        self.spell_tiers =[]
        for tier in self.spells_prepered.values():
            if tier == 'cantrip':
                pass
            else:
                self.spell_tiers.append(tier)

    def heal(self,entry):
        try:
            self.hp = int(self.hp)
            self.max_hp = int(self.max_hp)
            heal = entry
            self.hp += heal
            if self.hp > self.max_hp:
                self.hp = self.max_hp
        except ValueError:
            print('value error')
        except TypeError:
            print('value error')
    
    def damage(self,entry):
        try:
            self.hp = int(self.hp)
            damage = entry
            self.hp -= damage
            if self.hp < 0:
                self.hp = 0
        except ValueError as e:
            print('value error')
        except TypeError:
            print('value error')

    def spend_hit_dice(self):
        self.hit_dice =int(self.hit_dice)
        self.hit_dice -= 1
        if self.hit_dice < 0:
            self.hit_dice = 0
            return 'no more hit dice left'
        self.hp = int(self.hp)
        self.hp += (int(self.con) + 5)
        self.max_hp = int(self.max_hp)
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def short_rest(self):
        pass

    def long_rest(self):
        self.hp = self.max_hp
        self.hit_dice = self.max_hit_dice
        return 'long rest taken'