# excersize involving input() code, also includes cars


# quick loop to demonstrate if-then statement
cars_in_stock = ["audi", "bmw", 'subaru', 'toyota']


# asking "customer" about rental cars
prompt = "What is the brand of the car you are looking for?"
prompt += "\n\tReply: "
car_selected = input(prompt)
print(car_selected)

"""
for car in sorted(cars):
	if car == "bmw":
		print car.upper()
	else:
		print car.title()


# testing out how equality works
print("\ntesting out equality operator:")
car = 'bmw'
print(car == 'bmw')
car = 'audi'
print(car == 'bmw')
car = 'Audi'
print(car == 'audi')
car = 'Audi'
print(car.lower() == 'audi')
"""
