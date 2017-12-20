# List of Languages excersizes
# Languages that I can claim to know

"""
stages of human developement...

Baby (0)
Toddler (1 - 2)
Preschooler (3 - 4)
Main childhood (5 - 9)
Pre-teenager (10-12)
Teenager (13-19)
Twentysomething (20-29)
Thirtysomething (30-39)
Fortysomething (40-49)
Fiftysomething (50-59)
Sixtysomething (60-69)
Seventysomething (70-79)
Eightysomething (80-89)
Ninetysomething (90-99)
Centenarian (100-109)
Supercentenarian (110+)
"""

Languages = ["english", "chinese", "latin", "greek", "python"]
languages_learned = {
	"baby": "chinese",
	"toddler": "chinese",
	"preschooler": "chinese",
	"main childhood": "english",
	"teenager": "latin",
	"twentysomething": "programming",
	"thritysomething": "",
	"fortysomething": "",
	"fiftysomething": "",
	"sixtysomething": "",
	"seventysomething": "",
	"eightysomething": "",
	"ninetysomething": "",
	"centenarian": "",
	"supercentenarian": "",
	}

lived_through_stages = ['baby', 'toddler', 'preschooler', 'main childhood',
						'teenager', 'twentysomething']

for stage, language in languages_learned.items():
	if stage in lived_through_stages:
		print("During my " + stage + " years, I've studied " + language + ".")
	elif stage not in lived_through_stages:
		print("During my " + stage + " years, I've yet to study.")
