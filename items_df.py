import numpy as np
import json
import pandas as pd

with open('./cleaned_data/items.json', 'r') as file:
    data = json.load(file)

df = pd.json_normalize(data['itemGroup'])

def main(data):
    for row in data['itemGroup']:
         print(row)

def del_key():
    del data['_meta']
    return data

def save_data(data):
    with open('./cleaned_data/items.json','w') as file:
        json.dump(data, file,indent=4)
if __name__ == "__main__":
    # data = del_key()
    print(df.info())
    # save_data(data)
    
