
class Character:
    def __init__(self,name,max_hp,max_hit_dice):
        self.max_hp = max_hp
        self.hp = self.max_hp
        self.name = name
        self.max_hit_dice = max_hit_dice
        self.hit_dice = 5
        
        self.spells_prepered = {
                                'Eldritch Blast':'cantrip',
                                'Armor of Aghatys': 'tier 1',
                                'Invisibility': 'tier 2'}
        self.max_prepered_spells = 2
        
        self.stre=0
        self.dex = 0
        self.con = 3
        self.inte = 0
        self.wis =0
        self.cha=0
        self.lvl=1
        self.short_rest_abilities =[]
        self.long_rest_abilities=[]

    

    def heal(self,entry):
        try:
            heal = int(entry.get())
            self.hp += heal
            if self.hp > self.max_hp:
                self.hp = self.max_hp
        except ValueError:
            print('value error')
    
    def damage(self,entry):
        try:
            damage = int(entry.get())
            self.hp -= damage
            if self.hp < 0:
                self.hp = 0
        except ValueError as e:
            print('value error')

    def spend_hit_dice(self):
        self.hit_dice -= 1
        if self.hit_dice < 0:
            self.hit_dice = 0
            return 'no more hit dice left'
        self.hp += (self.con + 5)
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def short_rest(self):
        pass

    def long_rest(self):
        self.hp = self.max_hp
        self.hit_dice = self.max_hit_dice
        return 'long rest taken'