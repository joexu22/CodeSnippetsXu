# Making a Pizza Restaurant - 

# This the the pizza menu
pizza_menu = [
	"pepperoni",
	"mushrooms",
	"onions",
	"sausage",
	"bacon",
	"extra cheese",
	"black olives",
	"green peppers",
	"pineapple",
	"spinach",
	]

ordering_prompt = "What topping would you like to have on your pizza?:"
ordering_prompt += "\n(type 'quit' when you are done selecting) "

order_ready = False
toppings_ordered = []
while not order_ready:
	topping = input(ordering_prompt)
	if topping == 'quit':
		order_ready = True
	elif topping not in pizza_menu:
		print("Apologies, we do not carry that topping; try again")
	else:
		toppings_ordered.append(topping)
		toppings_ordered = list(set(toppings_ordered)) # handle duplicates
		
print("\nyour pizza:".title())
print("Here is your pizza with the following toppings: ")
for topping in toppings_ordered:
	print("\t" + topping)
