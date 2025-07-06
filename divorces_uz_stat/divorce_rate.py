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
areas = list(divorce_rate['Klassifikator_ru'])[:]
years = [str(y) for y in range(2010,2024)]
divorce_rate_new = pd.DataFrame(index=areas, columns=['Maximum divorces','Minimum divorces','Average divorces'])
end_stat = []

#print(divorce_rate.loc[areas.index('Кашкадарьинская область')]['2010'])
#print(divorce_rate_new)

for i in areas:
    if(i != 'Республика Узбекистан'):
        divorce_rate_new.loc[i,'Maximum divorces'] = (divorce_rate.loc[areas.index(i),years].max())
        divorce_rate_new.loc[i, 'Minimum divorces'] = (divorce_rate.loc[areas.index(i), years].min())
        divorce_rate_new.loc[i, 'Average divorces'] = (divorce_rate.loc[areas.index(i), years].mean())

end_stat.append(f'Average : {float(divorce_rate_new['Average divorces'].mean())}')
end_stat.append(f'Minimum : {float(divorce_rate_new['Minimum divorces'].min())}')
end_stat.append(f'Maximum : {float(divorce_rate_new['Maximum divorces'].max())}')
print(end_stat)
print(divorce_rate_new)
print(areas)