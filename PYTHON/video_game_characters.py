# Practice excersize involving dictionaries
person_1 = {'first_name': 'Gordon', 'last_name': 'Freeman',
			'age': 27, 'city': 'Seattle'}
person_2 = {'first_name': 'Mario', 'last_name': 'Mario',
			'age': 24, 'city': 'Mushroom Kingdom'}
person_3 = {'first_name': 'Lara', 'last_name': 'Croft',
			'age': 21, 'city': 'Wimbledon'}
person_4 = {'first_name': 'Link', 'last_name': 'Link', 
			'age': 17, 'city': 'Hyrule'}
person_5 = {'first_name': 'Cloud', 'last_name': 'Strife',
			'age': 21, 'city': 'Nibelheim'}
person_6 = {'first_name': 'Pikachu', 'last_name': 'Ketchum',
			'age': 17, 'city': 'Pallet Town'}

# attempt at building a dictionary within a dictionary
characters = {}
characters.update(dict(person_1=person_1))
characters.update(dict(person_2=person_2))
characters.update(dict(person_3=person_3))
characters.update(dict(person_4=person_4))
characters.update(dict(person_5=person_5))
characters.update(dict(person_6=person_6))
import pprint # prints readable material
pprint.pprint(characters)


# Name's and numbers
favorite_number_1 = {"Winston": 22}
favorite_number_2 = {"Nasus": 1}
favorite_number_3 = {"Garrosh": 30}
favorite_number_4 = {"Sniper": 7}
favorite_number_5 = {"Counter Terrorist": 13}

favorite_number = {"Winston": 22,
				   "Nasus": 1,
				   "Garrosh": 30,
				   "Sniper": 7,
				   "Counter Terrorist": 13}
