from random import randint

def d4():
    return randint(1,4)
def d6():
    return randint(1,6)
def d8():
    return randint(1,8)
def d10():
    return randint(1,10)
def d12():
    return randint(1,12)
def d20():
    return randint(1,20)
def d100():
    return randint(1,100)
def dY(y_sided):
    return randint(1,y_sided)

def roll_adv():
    pass

def roll_disadv():
    pass

def many_same_dice(amount,dice_function):
    ltotal= []
    for i in range(amount):
        roll =dice_function()
        ltotal.append(roll)
    itotal = sum(ltotal)
    return ltotal,itotal

def many_mixed_dice(mixed_amount,same_amount,dice_function):
    pass

if __name__=='__main__':
    print(many_same_dice(5,d6))
