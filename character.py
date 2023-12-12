
class Character:
    def __init__(self,max_hp,hp,name):
        self.max_hp = max_hp
        self.hp = hp
        self.name = name
    
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

    