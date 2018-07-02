# Excersize involving inequality operator


# taking equality out for a test
requested_toppings = 'mushrooms'
if requested_toppings != 'anchovies':
	print("hold the anchovies!")
	

# number comparison examples
print("\nnumber comparisons:")
age = 18
print(age == 18)

answer = 17
if answer != 42:
	print("That is not the correct answer. Please try again!")

	
# various inequalities
age = 19
print(age < 21)
print(age <= 21)
print(age > 21)
print(age >= 21)


# multiple conditions (and)/(or)
print("\ntesting out (and)/(or):")
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)
age_1 = 21
print(age_0 >= 21 and age_1 >= 21)

age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)
age_0 = 18
print(age_0 >= 21 or age_1 >= 21)


# checking if value is in a list
print("\nchecking values (in) a list:")
requested_toppings = ['mushrooms', 'onions', 'pineapples']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)


print("\nMaking of a Pizza:")
available_toppings = ["mushrooms","olives","green peppers",
					  "pepperoni","pineapple","extra cheese"]
requested_toppings = ["mushrooms","frech fries","extra cheese"]
for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")
