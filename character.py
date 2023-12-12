
class Character:
    def __init__(self,max_hp,hp,name):
        self.max_hp = max_hp
        self.hp = hp
        self.name = name
        self.max_hit_dice = 5
        self.hit_dice = 5
        self.con = 3
        self.spells_prepered = {
                                'Eldritch Blast':'cantrip',
                                'Armor of Aghatys': 'tier 1',
                                'Invisibility': 'tier 2'}
        self.max_prepered = 2
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