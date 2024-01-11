from random import randint
from copy import deepcopy

class Dice:
    def __init__(self):
        self.standard_dice = [
            self.d4,self.d6,self.d8,
            self.d10,self.d12,
            self.d20,self.d100
]       
        self.y_side = None

        self.multipliers =[]
        self.modifier =0
        self.names =['d4','d6','d8','d10',
                     'd12','d20','d100']
        

        self.damage_dice = {
            'd4':self.d4,
            'd6':self.d6,
            'd8':self.d8,
            'd10':self.d10,
            'd12':self.d12
        }
        
        self.damage_types= [
            'Slashing',
            'Piercing',
            'Bludgeoning',
            'Fire',
            'Cold',
            'Lightning',
            'Thunder',
            'Acid',
            'Poison',
            'Necrotic',
            'Radiant',
            'Psychic',
            'Force'
        ]


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
            return total,rolls,self.names[dice_index]
        
        try:
            for i in range(amount):
                roll = self.dY(y_side)
                rolls.append(roll)
            total = sum(rolls)
            return total,rolls,f'd{y_side}'
        except TypeError:
            return 0,[]
    
    def roll_all(self):
        all_rows = []
        for i,mult in enumerate(self.multipliers):
            roll_row = self.roll_dice_row(mult,i,self.y_side)
            all_rows.append(roll_row)
        self.all_rolls = all_rows
        return all_rows
  
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
    
    def text_boxing(self):
        total =0
        all_texts =[]
        for row in self.all_rolls:
            if row[0] !=0:
                total+= row[0]
                text_row = f'{row[2]}: {row[1]} -> {row[0]}'
                all_texts.append(text_row)
        total+= self.modifier
        all_texts.append(f'Total {total}')
        return all_texts
    
    def clean_modifier(self,mod):
        try:
            mod = int(mod.get())
        except Exception:
            mod =0
        self.modifier = mod

    def clean_large_attacks(self,amount,modifier,AC,adv,disadv):
        amount = amount.get()
        if amount.isnumeric() and amount!='0':
            amount = int(amount)
        else:
            amount =1

        try:
            modifier = int(modifier.get())
        except Exception:
            modifier =0
        
        AC = AC.get()
        if AC.isnumeric():
            AC = int(AC)
        else:
            AC =10

        adv = adv.get()
        disadv = disadv.get()
    
        out = {
            'amount':amount,
            'modifier':modifier,
            'AC':AC,
            'adv':adv,
            'disadv':disadv
        }
        return out
    
    def get_all_damage_matrix(self,all_dice_matrix):
        out_all=[]
        for matrix in all_dice_matrix:
            out_matrix ={}
            for key,val in matrix.items():
                if key == 'name':
                    out_matrix[key] = val
                elif key =='modifier':
                    try:
                        val = int(val.get())
                        out_matrix[key] = val
                    except Exception:
                        val =0
                        out_matrix[key] = val
                elif key =='amount':
                    val = int(val.get())
                    out_matrix[key] = val
                else:
                    val = val.get()
                    out_matrix[key] = val

            out_all.append(out_matrix)
        return out_all
                
    def roll_large_attacks(self,attack_matrix):
        attacks = []
        for i in range(attack_matrix['amount']):
            if attack_matrix['adv'] == False and attack_matrix['disadv'] == False:
                roll = self.roll_attack(attack_matrix['modifier'],
                                        attack_matrix['AC'])
            elif attack_matrix['adv']:
                roll = self.roll_attack(attack_matrix['modifier'],
                                        attack_matrix['AC'],adv=True)
            
            else:
                roll = self.roll_attack(attack_matrix['modifier'],
                                        attack_matrix['AC'],adv=False)
            attacks.append(roll)
        return attacks
    
    def evaluate_hits(self,attacks):
        hits=0
        crits=0
        for attack in attacks:
            if attack[0] =='crit':
                crits+=1
            elif attack[0] == 'hit':
                hits+=1
        return hits,crits

    def roll_attack(self,modifier,AC,adv=None):
        if adv == None:
            roll= self.d20()
        elif adv:
            roll = self.roll_adv(self.d20)
        else:
            roll = self.roll_disadv(self.d20)

        if roll == 20:
            return 'crit',roll+modifier
        elif roll == 1:
            return 'miss',roll+modifier
        elif (roll+modifier) >= AC:
            return 'hit',roll+modifier
        else:
            return 'miss',roll+modifier
        
    def roll_adv(self,dice_function):
        roll1 = dice_function()
        roll2 = dice_function()
        return max(roll1,roll2)
    
    def roll_disadv(self,dice_function):
        roll1 = dice_function()
        roll2 = dice_function()
        return min(roll1,roll2)

    def format_damage_dice(self,dice_matrix):
        amount = dice_matrix['amount']
        name =dice_matrix['name']
        mod = dice_matrix['mod']
        dtype =dice_matrix['type']
        text = f'{amount}{name}+{mod} {dtype}\n'
        return text

    
    def dmg_by_type(self):
        dmg_by_type = {}
        for dtype in self.damage_types:
            dmg_by_type[dtype] = {}
        
        for dtype,value in dmg_by_type.items():
            for dice_type in self.damage_dice.keys():
                value[dice_type] = []
        return dmg_by_type
        
    def roll_damage_1(self,amount,dice_function,mod,crit=False):
        rolls=[] 
        total = 0
        if not crit:
            for i in range(amount):
                roll = self.damage_dice[dice_function]()
                rolls.append(roll)
            if amount !=0:
                total = sum(rolls)
         
        else:
            for i in range(amount*2):
                roll = self.damage_dice[dice_function]()
                rolls.append(roll)
            if amount !=0:
                total = sum(rolls)

        return (rolls,total)

    def roll_all_damage_1(self,landed_atks,all_damage_matrix):
        hits = landed_atks[0]
        crits = landed_atks[1]
        dmg_by_type = self.dmg_by_type()
        values = []

        # hits
        for matrix in all_damage_matrix:
            if matrix["type"] in dmg_by_type:
                amount = matrix["amount"]
                name = matrix["name"]
                mod = matrix["mod"]
                dtype = matrix["type"]
                crit = False
                total_dice = hits*amount

                roll = self.roll_damage_1(amount=total_dice,
                    dice_function=name,mod=mod,crit=crit)
                total = roll[1] +mod*hits
                rolls = roll[0]

                values.append((rolls,mod,total,
                        name,dtype,crit))
                
        # crits
        for matrix in all_damage_matrix:
            if matrix["type"] in dmg_by_type:
                amount = matrix["amount"]
                name = matrix["name"]
                mod = matrix["mod"]
                dtype = matrix["type"]
                crit = True
                total_dice = amount*crits

                roll = self.roll_damage_1(amount=total_dice,
                    dice_function=name,mod=mod,crit=crit)
                total = roll[1] +mod*crits
                rolls = roll[0]

                values.append((rolls,mod,total,
                        name,dtype,crit))
        
        for instance in values:
            rolls = instance[0]
            mod = instance[1]
            total = instance[2]
            name = instance[3]
            dtype = instance[4]
            crit = instance[5]
            filterd_vals = (rolls,mod,total,crit)
            if dtype in dmg_by_type:
                if name in dmg_by_type[dtype]:
                    dmg_by_type[dtype][name].append(filterd_vals)

        return dmg_by_type
        
            
# to be removed
    def roll_damage(self,dice_function,modifier,crit=False):
        if crit:
            roll1 = dice_function()
            roll2 = dice_function()
            roll = roll1+roll2+modifier
            return roll
        else:
            roll = dice_function() + modifier
            return roll

    def roll_all_damage_with_hits(self,hits,all_damage_matrix):
        hit = hits[0]
        crit = hits[1]
        hit_out = []
        crit_out=[]

        texts ={}
        for dtype in self.damage_types:
            texts[dtype] = []

        for i in range(hit):
            roll = self.roll_all_damage(all_damage_matrix,False)
            hit_out.append(roll)
        
        for i in range(crit):
            roll = self.roll_all_damage(all_damage_matrix,True)
            
            crit_out.append(roll)
 
    def roll_all_damage(self,all_damage_matrix,crit):
        rolls=[]
        for row in all_damage_matrix:
            matrix = self.roll_damage_matrix(row,crit=crit)
            rolls.append(matrix)
        return rolls

    def roll_damage_matrix(self,dice_matrix,crit):
        rolls = []        
        for i in range(dice_matrix['amount']):
            tag=self.damage_dice[dice_matrix['name']]
            roll = self.roll_damage(tag,
                    dice_matrix['mod'],crit=crit)
            rolls.append(roll)

        total = sum(rolls)
        out = {
            'name':dice_matrix['name'],
            'type':dice_matrix['type'],
            'total':total,
            'array':rolls
        }
        return out
            
    def sort_damage_type(self,all_damage):
        hits = all_damage[0]
        crits = all_damage[1]
        
        for hit in hits:
            ohits = self.damage_to_dict(hit,crit=False)
            
        for crit in crits: 
            ocrits= self.damage_to_dict(crit,crit=True)
            
        merged_dict = ohits.copy()
        for key, value in ocrits.items():
            if key not in merged_dict:
                merged_dict[key] = value
            else:
                merged_dict[key].extend(value)

        return merged_dict
        
    def damage_to_dict(self,damages,crit=False):
        texts ={}
        for dtype in self.damage_types:
            texts[dtype] = []

        for damage in damages:
            dtype= damage['type']
            del damage['type']
            damage['crit'] = crit
            texts[dtype].append(damage)
        return texts

    def clean_damage_1(self,all_damage_matrix,landed_atks):
        hits=landed_atks[0]
        crits=landed_atks[1]
        
        out_dict ={}
        for dtype in self.damage_types:
            out_dict[dtype] = []

        hit_dict = out_dict.copy()
        crit_dict = out_dict.copy()

        for dmg in all_damage_matrix:
            dice_total = dmg['amount'] * hits
            dice_type = self.damage_dice[dmg['name']]
            mod = dmg['mod']
            dtype = dmg['type']
            rolls = []
            if dice_total !=0:
                for i in range(dice_total):
                    roll = self.roll_damage(dice_function=dice_type,
                        modifier=mod,crit=False)
                    rolls.append(roll)
                total = sum(rolls)
                hit_dict[dtype].append([rolls,total,dmg['name'],False])

        for dmg in all_damage_matrix:
            dice_total = dmg['amount'] * crits
            dice_type = self.damage_dice[dmg['name']]
            mod = dmg['mod']
            dtype = dmg['type']
            rolls = []
            if dice_total !=0:
                for i in range(dice_total):
                    roll = self.roll_damage(dice_function=dice_type,
                        modifier=mod,crit=True)
                    rolls.append(roll)
                total = sum(rolls)
                crit_dict[dtype].append([rolls,total,dmg['name'],True])
    
        total =self.clean_damage_2(hit_dict=hit_dict)
        return total
    
    def clean_damage_2(self,hit_dict):
        total = 0
        allparsed_dmg=[]
        for dtype,values in hit_dict.items():
            if values != []:
                type_total = self.get_total_dmg(values)
                total += type_total
                parsed_dmg =self.parse_damage(dtype,values)
                allparsed_dmg.append(parsed_dmg)
        return total,allparsed_dmg

    def parse_damage(self,dtype,values):
        out = {dtype:[]}
        
        for value in values:
            if value[3]:
                crit = value[0],value[1],value[2],value[3]
                out[dtype].append(crit)
            else:
                hit = value[0],value[1],value[2],value[3]
                out[dtype].append(hit)
        return out
        
    def get_total_dmg(self,values):
        total =0
        for value in values:
            total+=value[1]
        return total
    

if __name__=='__main__':
    d = Dice()
    print(d.roll_one_damage_type())
