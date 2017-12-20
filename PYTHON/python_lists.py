# an examination into the workings of python lists
family_members = ['dad', 'mom', 'mike', 'me']
print(family_members)

# printing first in list
print(family_members[0])

# print title()
print(family_members[0].title())

# print last item
print(family_members[-1].title())

# messaging time
message = "My brother is " + family_members[2].title() + "."
print(message)

# list replacement
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

# append to list
motorcycles.append('honda')
print(motorcycles)

# building a list
motorcycles = []
print(motorcycles)
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# list insert
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

# delete item in a list
print("\ndeleting items:".title())
print(motorcycles)
del motorcycles[0]
print(motorcycles)

# poping a item from a list
print("\npoping items:".title())
motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# application of popped item
# poping a item from a list
print("\napplying pop():".title())
motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop()
print("a very decent motorcycle is " + popped_motorcycle.title() + ".")

# removing item by value
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

# sort lists
print("\nsorting excersize")
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

# understanding temperatory sorting
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere's the sorted list in reverse")
print(sorted(cars, reverse=True))
print("\nHere is the original list again:")
print(cars)

# *Quick excersize on sorting capital letters
test_string = "This is a test string from Andrew"
print("\ntest case for capital letters:".title())
print(sorted(test_string.split(), key=str.lower))

# length of cars
cars = ['bmw', 'audi', 'toyoya', 'sudbaru']
print("\nthere are " + str(len(cars)) + " car companies in the specified list")
