from random import randint

class Dice:
    def __init__(self):
        self.standard_dice = [
            self.d4,self.d6,self.d8,
            self.d10,self.d12,
            self.d20,self.d100
]       
        self.y_side = None

        self.multipliers =[]

        self.names =['d4','d6','d8','d10',
                     'd12','d20','d100']

    def d4(self):
        return randint(1,4)
    
    def d6(self):
        return randint(1,6)
    
    def d8(self):
        return randint(1,8)
    
    def d10(self):
        return randint(1,10)
    
    def d12(self):
        return randint(1,12)
    
    def d20(self):
        return randint(1,20)
    
    def d100(self):
        return randint(1,100)
    
    def dY(self,y_sided):
        if y_sided ==0:
            raise TypeError
        else:
            return randint(1,y_sided)
    
    
    def roll_dice_row(self,amount,dice_index,y_side):
        rolls=[]
        if dice_index !=7:
            for i in range(amount):
                roll = self.standard_dice[dice_index]()
                rolls.append(roll)
            total = sum(rolls)
            return total,rolls
        
        try:
            for i in range(amount):
                roll = self.dY(y_side)
                rolls.append(roll)
            total = sum(rolls)
            return total,rolls
        except TypeError:
            return 0,[]
    
    def roll_all(self):
        all_rows = []
        for i,mult in enumerate(self.multipliers):
            roll_row = self.roll_dice_row(mult,i,self.y_side)
            all_rows.append(roll_row)
        print(all_rows)



    def many_mixed_dice(self,mixed_amount,same_amount,dice_function):
        pass
    
    def get_multipliers(self,iterable):
        '''Return List with int'''
        multipliers=[]
        for multiplier in iterable:
            multiplier = int(multiplier.get())
            multipliers.append(multiplier)
        return multipliers
    
    def add_multipliers(self,x1,x5):
        self.multipliers = [x + y*5 for x, y in zip(x1, x5)]
        return self.multipliers
        
    
    def setup_dY(self,y_side):
        try:
            if int(y_side.get()) !=0:
                self.y_side = int(y_side.get())
            else:
                self.multipliers.pop()     
        except ValueError:
            self.y_side = None
            self.multipliers.pop()       
        return self.y_side
    

    
  

    
    

    



if __name__=='__main__':
    d = Dice()
    
