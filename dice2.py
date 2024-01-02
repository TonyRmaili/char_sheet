

from random import randint

class Dice2:
    def __init__(self) -> None:
        pass
        
    def d4(self):
        return randint(1,4),'d4'
    
    def d6(self):
        return randint(1,6),'d6'
    
    def d8(self):
        return randint(1,8),'d8'
    
    def d10(self):
        return randint(1,10),'d10'
    
    def d12(self):
        return randint(1,12),'d12'
    
    def d20(self):
        return randint(1,20),'d20'
    
    def d100(self):
        return randint(1,100),'d100'
    

    def 