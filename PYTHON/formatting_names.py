# Python3 Excersize invovling formatting name

def get_formatted_name(first_name, last_name):
	"""returns a full name, fully formatted"""
	full_name = first_name + " " + last_name
	return full_name.title()
	
musician = get_formatted_name("jimi","hendrix")
print(musician)

# making middle name optional
def get_formatted_name(first_name, last_name, middle_name=""):
	"""Return a full name, neatly formatted."""
	if middle_name:
		full_name = first_name + ' ' + middle_name + ' ' + last_name
	else:
		full_name = first_name + ' ' + last_name
	return full_name.title()

musician = get_formatted_name("jimi","hendrix")
print(musician)
musician = get_formatted_name("john","hooker","lee")
print(musician)
