import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

hero_names = pd.read_csv('hero_names.csv')
A_heroes = hero_names['localized_name'][hero_names['localized_name'].str.startswith('A')] # statement where we check if heroes name startswith some letter

alphabet = {
    0: ['A', 0,0],
    1: ['B', 0,0],
    2: ['C', 0,0],
    3: ['D', 0,0],
    4: ['E', 0,0],
    5: ['F', 0,0],
    6: ['G', 0,0],
    7: ['H', 0,0],
    8: ['I', 0,0],
    9: ['J', 0,0],
    10: ['K', 0,0],
    11: ['L', 0,0],
    12: ['M', 0,0],
    13: ['N', 0,0],
    14: ['O', 0,0],
    15: ['P', 0,0],
    16: ['Q', 0,0],
    17: ['R', 0,0],
    18: ['S', 0,0],
    19: ['T', 0,0],
    20: ['U', 0,0],
    21: ['V', 0,0],
    22: ['W', 0,0],
    23: ['X', 0,0],
    24: ['Y', 0,0],
    25: ['Z', 0,0]
}
heroes_sorted = []

# in this loop i check how many heroes have names starting on alphabetical letters
for letter in alphabet:
    if(not hero_names['localized_name'][hero_names['localized_name'].str.startswith(alphabet[letter][0])].empty):
        #print(f' \nDota2 heroes with Name starting with letter {alphabet[letter][0]} : ')
        heroes_sorted.append(hero_names['localized_name'][hero_names['localized_name'].str.startswith(alphabet[letter][0])].tolist())
        alphabet[letter][1] += len(hero_names['localized_name'][hero_names['localized_name'].str.startswith(alphabet[letter][0])])
        #print('----------------')

print(alphabet)
print(heroes_sorted)
