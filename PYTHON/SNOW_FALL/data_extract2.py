"""
This file will extract data into only necessary data.
"""

import json
import os
import numpy
import pandas
from ast import literal_eval
from pandas import DataFrame


dir_path = os.path.dirname(os.path.realpath(__file__))
data_file = os.path.join(dir_path + '\\snowfall_data.txt')

SnowTabulation = []

with open(data_file, 'r') as outfile:
    data_array = literal_eval(outfile.read())
    for item in data_array:
        date_value = item.get("DATE")
        snow_value = item.get("SNOW")
        if snow_value == None:
            snow_value = 0
        SnowTabulation.append((date_value, snow_value))

df = DataFrame(SnowTabulation, columns = ['Date', 'Snowfall'])
df['Date'] = pandas.to_datetime(df['Date'])
df['Month'] = pandas.DatetimeIndex(df['Date']).month
df['Day'] = pandas.DatetimeIndex(df['Date']).day
df['Snowfall'] = df['Snowfall'].astype(int)

df_1 = df.drop(columns=['Date'])
df_2 = df_1.query('Snowfall > 3')
df_3 = df_2.groupby(['Month','Day']).count()
#print(df_3)
print(df_3.to_csv())