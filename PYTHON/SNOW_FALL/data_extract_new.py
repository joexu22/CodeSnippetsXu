"""
This file will extract data into only necessary data.
"""

import json
import os
import pprint
from ast import literal_eval
from datetime import datetime
from datetime import date

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

FirstSnowFall = {}
first_event_happened = True
for item in SnowTabulation:
    itemDateTime = date.fromisoformat(item[0]);
    if itemDateTime.month == 12 and itemDateTime.day == 15:
        first_event_happened = False
    if first_event_happened == False and int(item[1]) >= 3:
        FirstSnowFall[itemDateTime.month, itemDateTime.day] = FirstSnowFall.get((itemDateTime.month, itemDateTime.day), 0) + 1;
        first_event_happened = True

pprint.pprint(FirstSnowFall)


#snow_only_file = os.path.join(dir_path + '\\new_graph.txt')
#with open(snow_only_file, 'w') as writefile:
#    for item in SnowTabulation:
#        writefile.write("{},{}\n".format(item[0], item[1]))