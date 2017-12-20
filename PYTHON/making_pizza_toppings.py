# Pizza Functions - Arbitrary Arguments

def make_pizza(size, *toppings):
	"""testing a functions with an arbitrary number of arguments"""
	print("\nMaking a " + str(size) +
		  "in size pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)

make_pizza(16 ,'pepperoni')
make_pizza(12 ,'mushrooms','green peppers','extra cheese')
make_pizza(8, 'pepperoni')
