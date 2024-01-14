from flask import Flask, render_template, request, jsonify
from dice import Dice

app = Flask(__name__)
damage_matrixes = []
def store_attack_entry(amount,mod,AC,adv,disadv):
    atk_matrix = {
            'amount':amount,
            'modifier':mod,
            'AC':AC,
            'adv':adv,
            'disadv':disadv
        }
    return atk_matrix

def store_damage_entry(dice_amount,dice_type,
    modifier,damage_type):
    
    damage_matrix = {'amount': dice_amount,
                    'name': dice_type,
                    'mod': modifier,
                    'type': damage_type}
    damage_matrixes.append(damage_matrix)
    return damage_matrixes

def clean_dmg(dmg_by_type):
    out={}
    grand_total = []
    for dtype,dice_type in dmg_by_type.items():
        type_total = []
        for val in dice_type.values():
            for roll in val:
                total = roll[2]
                type_total.append(total)
        type_total = sum(type_total)
        out[dtype] = type_total
        grand_total.append(type_total)

    grand_total = sum(grand_total)
    out['Grand Total'] = grand_total
    return out
        

@app.route('/', methods=['GET','POST'])
def home():
    damage_matrixes = []
    if request.method == 'POST':
        dice_amount = int(request.form['dice_amount'])
        dice_type = request.form['dice_type']
        damage_modifier = int(request.form['damage_modifier'])
        damage_type = request.form['damage_type']

        damage_matrixes= store_damage_entry(dice_amount=dice_amount,
        dice_type=dice_type,modifier=damage_modifier,
        damage_type=damage_type)
        
    return render_template('index.html',damage_matrixes=damage_matrixes)

@app.route('/roll_atk',methods=['GET','POST'])
def roll_attacks_end():
    dice=Dice()
    if request.method == 'POST':
        atk_amount = int(request.form['atk_amount'])
        atk_mod = int(request.form['atk_mod'])
        ac = int(request.form['AC'])
        adv = request.form['adv']
        dis_adv = request.form['dis_adv']

        if adv =='True':
            adv = True
        else:
            adv =False
        
        if dis_adv =='True':
            dis_adv = True
        else:
            dis_adv =False

        if adv == True and dis_adv == True:
            adv=False
            dis_adv=False

        atk_matrix = store_attack_entry(
                amount=atk_amount,mod=atk_mod,AC=ac,
                adv=adv,disadv=dis_adv
            )
        roll_atks = dice.roll_large_attacks(attack_matrix=atk_matrix)
        landed_atks = dice.evaluate_hits(attacks=roll_atks)

        dmg_by_type=dice.roll_all_damage_1(landed_atks=landed_atks,all_damage_matrix=damage_matrixes)
        cleaned_dmg=clean_dmg(dmg_by_type=dmg_by_type)

        return render_template("index.html",attacks=cleaned_dmg,landed_atks=landed_atks)

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
    
