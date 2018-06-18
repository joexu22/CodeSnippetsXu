# return dictionaries in Python3

def build_person(first_name, last_name):
	"""Return a dictionary of information about a person."""
	person = {'first:': first_name, 'last': last_name}
	return person
	
musician = build_person('jimi','hendrix')
print(musician)

for person in musician.items():
	print(person)
