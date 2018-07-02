# Python3 excersize involving "Magicians"
# Best use of functions and lists...

magicians = [
	"ricky jay",
	"harry houdini",
	"criss angel",
	"the great lafayette",
	"derren brown",
	"apollo robbins",
	"dynamo",
	"jerry sadowitz",
	"penn and teller",
	"david blaine",
]

def show_magicians(magician_list):
	"""simple code used to print a list of magicians"""
	for magician in magician_list:
		output = "For today's show we have " + magician.title() + "!"
		print(output)

def make_great(magician_list):
	"""modifying a list"""
	
	# list for holding values
	great_magicians = []
	
	# need to use while loops to edit list
	# it seems that python lists are rather immune to operations
	while magician_list:
		new_title = "the Great " + magician_list.pop()
		great_magicians.append(new_title)
	
	# reconstructing the the python_list
	# taking the temp values of magician_list and reapplying them to empty list
	for magician in great_magicians:
		magician_list.append(magician)
	
	# return a list if need be (temp copy of list[:])
	return magician_list
		

great_magicians = make_great(magicians[:])
show_magicians(magicians)
show_magicians(great_magicians)
