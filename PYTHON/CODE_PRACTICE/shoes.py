# Python3 male shoes
# doing some research into the nature of shoes...

def log_shoe(company, model, **information):
	"""this is something about making shoes"""
	shoe = {}
	shoe['company'] = company
	shoe['model'] = model
	for info, data in information.items():
		shoe[info] = data
	return shoe
	
shoe_1 = log_shoe('vans', 'classic slip-on', size=11, color='grey')

print(shoe_1)
