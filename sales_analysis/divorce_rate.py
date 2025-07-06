import numpy as np
import pandas as pd

# Установить отображение всех строк
pd.set_option('display.max_rows', None)

# Установить отображение всех столбцов
pd.set_option('display.max_columns', None)

# Если нужно полностью без обрезки ширины
pd.set_option('display.max_colwidth', None)

divorce_rate_csv = 'dvrs_rate.csv'
divorce_rate = pd.read_csv(divorce_rate_csv)
areas = list(divorce_rate['Klassifikator_ru'])
divorce_rate_new = pd.DataFrame(index=areas, columns=['Maximum divorces','Miminum divorces','Áverage divorces'])

print(divorce_rate.loc[areas.index('Кашкадарьинская область')])
#print(divorce_rate_new)