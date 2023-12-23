import tkinter as tk
import json

with open('skills.json') as file:
    skills =json.load(file)

skill_list = {}
for name in skills['skill']:
    skill_list[name['name']] = False

print(skill_list)

['Acrobatics', 'Animal Handling',
  'Arcana', 'Athletics', 'Deception',
    'History', 'Insight', 'Intimidation',
    'Investigation', 'Medicine', 'Nature', 
    'Perception', 'Performance', 'Persuasion', 
    'Religion', 'Sleight of Hand', 'Stealth', 'Survival']