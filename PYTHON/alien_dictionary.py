# working with Python3 dictionaries
# making cool alien ships...


# initialize aliens
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
	print(alien['color'])
	print(alien['points'])


# operating on alien_0 data
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")


# viewing dictionaries
print(alien_0)


# adding new key-value pairs
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)


# starting with empty dictionaries
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)


# modifying alien colors
alien_0 = {'color': 'green'}
print("\nThe alien is now " + alien_0['color'])
alien_0 = {'color': 'yellow'}
print("\nThe alien is now " + alien_0['color'])


# moving alien position
print("\ntracking alien position")
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))


# moving the alien to the right
# determine how far the alien moves based on its current speed
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3


# the new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))


# deleting keys
print("\ndeleting dictionary keys:")
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)


# creating a mass of aliens (30 aliens)
print("\ncreating a mass of aliens!:".title())
aliens = []
for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)


# changing up some of the aliens
for alien in aliens[0:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10

for alien in aliens[0:1]:
	if alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['speed'] = 'fast'
		alien['points'] = 15

	
# showing first 5 aliens
for alien in aliens[:5]:
	print alien
print("...")


# show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens)))
