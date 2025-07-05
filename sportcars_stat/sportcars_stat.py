import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Установить отображение всех строк
pd.set_option('display.max_rows', None)

# Установить отображение всех столбцов
pd.set_option('display.max_columns', None)

# Если нужно полностью без обрезки ширины
pd.set_option('display.max_colwidth', None)

sportcars_orig = pd.read_csv('sportcars.csv')
car_makers = sorted(list(set(sportcars_orig['Car Make'])))
sportcars_stat = pd.DataFrame(index = car_makers, columns = sportcars_orig.columns[1:])
sportcars_stat = sportcars_stat.drop('Year',axis = 1)
sportcars_stat = sportcars_stat.drop('Car Model',axis = 1)
sportcars_orig['Price (in USD)'] = sportcars_orig['Price (in USD)'].str.replace(',', '').astype(float)
sportcars_orig['0-60 MPH Time (seconds)'] = sportcars_orig['0-60 MPH Time (seconds)'].str.replace('<','').astype(float)
sportcars_orig['Torque (lb-ft)'] = pd.to_numeric(sportcars_orig['Torque (lb-ft)'].str.replace('-', ''),errors='coerce')
sportcars_orig['Horsepower'] = pd.to_numeric(sportcars_orig['Horsepower'],errors='coerce')
sportcars_orig['Engine Size (L)'] = pd.to_numeric(sportcars_orig['Engine Size (L)'],errors='coerce')

for model in car_makers:
   sportcars_stat.loc[model,'Price (in USD)'] = (sportcars_orig[sportcars_orig['Car Make'] == model]['Price (in USD)'].mean().astype(int))
   sportcars_stat.loc[model,'0-60 MPH Time (seconds)'] = (sportcars_orig[sportcars_orig['Car Make'] == model]['0-60 MPH Time (seconds)'].mean().astype(int))
   sportcars_stat.loc[model,'Torque (lb-ft)'] = (sportcars_orig[sportcars_orig['Car Make'] == model]['Torque (lb-ft)'].mean().astype(int))
   sportcars_stat.loc[model,'Horsepower'] = (sportcars_orig[sportcars_orig['Car Make'] == model]['Horsepower'].mean().astype(int) )
   sportcars_stat.loc[model,'Engine Size (L)'] = (sportcars_orig[sportcars_orig['Car Make'] == model]['Engine Size (L)'].mean())

#print(Lamborghini)
#print(car_makers)


print(sportcars_stat)

sportcars_stat.to_csv('sportcars_stat.csv')



