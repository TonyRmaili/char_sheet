from flask import Flask, render_template, request
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



@app.route('/', methods=['GET', 'POST'])
def home():
    dice=Dice()
    if request.method == 'POST':
        atk_amount = int(request.form['atk_amount'])
        atk_mod = int(request.form['atk_mod'])
        ac = int(request.form['AC'])
        adv = request.form['adv']
        dis_adv = request.form['dis_adv']

        dice_amount = int(request.form['dice_amount'])
        dice_type = request.form['dice_type']
        damage_modifier = request.form['damage_modifier']
        damage_type = request.form['damage_type']

        damage_matrixes= store_damage_entry(dice_amount=dice_amount,
        dice_type=dice_type,modifier=damage_modifier,
        damage_type=damage_type)
        
        atk_matrix = store_attack_entry(
            amount=atk_amount,mod=atk_mod,AC=ac,
            adv=adv,disadv=dis_adv
        )
        rolled_atks=dice.roll_large_attacks(attack_matrix=atk_matrix)
        landed_atk = dice.evaluate_hits(attacks=rolled_atks)

        print(landed_atk)
        
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
    
