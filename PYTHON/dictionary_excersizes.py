# Practice excersize involving dictionary
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

programming_concept_1 = {"Program Structure":
						 "Overall form of the product" +
						 "with an emphasis on individual components"}
programming_concept_2 = {"Variables":
						 "A way to store some information"}
programming_concept_3 = {"Loops":
						 "Ability to run code repetitively"}
programming_concept_4 = {"Control Structures": 
						 "Allowing the code to flow"}
programming_concept_5 = {"Syntax": 
						 "Rules defining the makeup of a program"}

# programming_concepts = {**programming_concept_1, **programming_concept_2}
programming_concepts = {}
programming_concepts.update(programming_concept_1)
programming_concepts.update(programming_concept_2)
programming_concepts.update(programming_concept_3)
programming_concepts.update(programming_concept_4)
programming_concepts.update(programming_concept_5)
print(programming_concepts)

print("\nUnpacking dictionary values:")
for key, value in programming_concepts.items():
	print(key + ":\n\t" + value)
	
favorite_languages = {
	'jen': 'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
	}

for name, language in favorite_languages.items():
	print("\nName: " + name.title() + "\nLanguage:" + language.title())

print("\nTracking dictionary keys")
for key in favorite_languages.keys():
	print(key.title())
for key in favorite_languages.items():
	print(key) # this returns a tuple
	print(key[0].title())

friends = ['phil','sarah']
for name in sorted(favorite_languages.keys()):
	print(name.title())
	if name in friends:
		print("\tHi " + name.title() + ", I see your favorite language is " +
			  favorite_languages[name].title() + "!")
if 'erin' not in favorite_languages.keys():
	print("Erin, please take our poll!")

print("\nThe following values have been mentioned:")
for language in set(favorite_languages.values()):
	print(language.title())
