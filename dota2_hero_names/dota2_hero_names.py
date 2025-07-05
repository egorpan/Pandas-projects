import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

hero_names = pd.read_csv('hero_names.csv')
A_heroes = hero_names['localized_name'][hero_names['localized_name'].str.startswith('A')] # statement where we check if heroes name startswith some letter

alphabet = {
    0: ['A', 0],
    1: ['B', 0],
    2: ['C', 0],
    3: ['D', 0],
    4: ['E', 0],
    5: ['F', 0],
    6: ['G', 0],
    7: ['H', 0],
    8: ['I', 0],
    9: ['J', 0],
    10: ['K', 0],
    11: ['L', 0],
    12: ['M', 0],
    13: ['N', 0],
    14: ['O', 0],
    15: ['P', 0],
    16: ['Q', 0],
    17: ['R', 0],
    18: ['S', 0],
    19: ['T', 0],
    20: ['U', 0],
    21: ['V', 0],
    22: ['W', 0],
    23: ['X', 0],
    24: ['Y', 0],
    25: ['Z', 0]
}
heroes_sorted = []

heroes_sorted_df = pd.Series()


# in this loop i check how many heroes have names starting on alphabetical letters
for letter in alphabet:
    if(not hero_names['localized_name'][hero_names['localized_name'].str.startswith(alphabet[letter][0])].empty):
        heroes_sorted.append(hero_names['localized_name'][hero_names['localized_name'].str.startswith(alphabet[letter][0])].tolist())
        alphabet[letter][1] += len(hero_names['localized_name'][hero_names['localized_name'].str.startswith(alphabet[letter][0])])
        heroes_sorted_df[f'{alphabet[letter]}'] = hero_names['localized_name'][hero_names['localized_name'].str.startswith(alphabet[letter][0])].tolist()

# at the end there is series of hero names with amount and letter
print(heroes_sorted_df)