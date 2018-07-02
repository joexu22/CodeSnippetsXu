# Coding excersizes showcasing if-then statements


# quick loop to demonstrate if-then statement
cars = ["audi", "bmw", 'subaru', 'toyota']
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

