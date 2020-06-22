"""
This file will extract data into only necessary data.
"""

import json
import os
from ast import literal_eval
from datetime import datetime

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

snow_only_file = os.path.join(dir_path + '\\tabulation.txt')
with open(snow_only_file, 'w') as writefile:
    for item in SnowTabulation:
        writefile.write("{},{}\n".format(item[0], item[1]))