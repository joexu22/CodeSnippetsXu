#  Dictionary of rivers...

river_dictionary = {
	'amazon': 'brazil',
	'nile': 'egypt',
	'yangtze': 'china',
	'yellow': 'china',
	'parana': 'argentina'
	}
	
for river, country in river_dictionary.items():
	print("The " + river.title() + " runs through " + country.title() + ".")
