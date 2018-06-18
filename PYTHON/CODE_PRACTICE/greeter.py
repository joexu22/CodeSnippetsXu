# furter application of of user input()
# using functions in conjunction


# application of functions
def get_formatted_name(first_name, last_name):
	"""Returns a neatly formatted name"""
	full_name = first_name + ' ' + last_name
	full_name.title()
	return full_name

# application of input()
while True:
	prompt = "\nPlease tell me your name:"
	prompt += "\n(enter 'q' at any time to quit)"
	print(prompt)
	
	first_name = input("Please tell me your first name: ")
	if first_name == 'q':
		break
	
	last_name = input("Please tell me your last nane: ")
	if last_name == 'q':
		break
	
	name = get_formatted_name(first_name, last_name)
	print ("Hello and Welcome, " + name + "!")
	break
