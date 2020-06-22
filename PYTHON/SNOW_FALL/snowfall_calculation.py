import requests
import json
import os

Save_Path = "c:\\Users\\JoeXu\\GitStuff\\CodeSnippetsJoe\\PYTHON\\SNOW_FALL\\"

URL = "https://www.ncei.noaa.gov/access/services/data/v1"

Datasets = "?dataset=daily-summaries"
Station_Identifiers = "&stations=USW00093738"
Start_Date = "&startDate=1941-12-07"
End_Date = "&endDate=2019-12-07"
Format="&format=json"

URL_Request = URL+Datasets+Station_Identifiers+Start_Date+End_Date+Format

response = requests.get(URL_Request)
data = response.content.decode("utf-8")

for entry in data:
	print(type(entry))

with open(Save_Path+'snowfall_data.txt', 'w') as outfile:
	#json.dump(response.content, outfile)
	outfile.write(response.content.decode("utf-8"))

snow_only_file = os.path.join(Save_Path + '\\tabulation.txt')
with open(snow_only_file, 'w') as writefile:
	for item in data:
		writefile.write(item)
