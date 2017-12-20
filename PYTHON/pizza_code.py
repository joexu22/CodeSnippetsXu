# Pizza Code that describes how to duplicate a list, without having the
# variable point to the same list location


pizza_list = ["pepperoni", "cheese", "susage"]

# doing this does not make two distinct lists
friend_pizza = pizza_list  # bad code

# need to do a slice...
friend_pizza = pizza_list[:]

pizza_list.append("mushroom")
friend_pizza.append("anchovie")


for pizza in pizza_list:
    print("My favorite pizzas are: " + pizza)

for pizza in friend_pizza:
    print("My friends favorite pizzas are: " + pizza)


# making my pizza with a dictionary
my_pizza = {
	'crust': 'thin',
	'toppings': ['pepperoni','garlic','mushrooms'],
	}

print("\nmy pizza:".title())
print("I like my pizza with a " + my_pizza['crust'] + " crust, " +
	  "with the following toppings:")
for topping in my_pizza['toppings']:
	print("\t" + topping)
