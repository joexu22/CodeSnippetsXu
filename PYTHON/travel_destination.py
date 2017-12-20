# Python3 code involving Travel Destinations


# Travel Desination Title
print("travel destinations".title())


# Places I want to visit wihin the next 5 years
destination_list = ["Santorini", "Apenzell", "Austin", "New York", "Portland"]


# Rather Good Looking Code
destination_dictionary = {
	"Santorini": {
		"location": 'greece',
		"best season": 0,
		"food": 0,
		"event": 0,
		},
	"Apenzell": {
		"location": 'switzerland',
		"best season": 0,
		"food": 0,
		"event": 0,
		},
	"Austin": {
		"location": 'texas',
		"best season": 0,
		"food": 0,
		"event": 0,
		},
	"New York": {
		"location": 'new york',
		"best season": 0,
		"food": 0,
		"event": 0,
		},
	"Portland": {
		"location": 'oregon',
		"best season": 0,
		"food": 0,
		"event": 0,
		},
	}


# Accessing the location of each city
print("\naccessing location from dictionary:".title())
for city_name, city_info in destination_dictionary.items():
	print("\nThe city of " + city_name + " is located in " + 
		  city_info['location'].title())


print("")
print("\nunsorted destination_list:".title())
print(destination_list)
print("\nsorted() destination_list:".title())
print(sorted(destination_list))
print("\nstill unsorted:".title())
print(destination_list)
print("\nsorted() destination_list in reverse:".title())
print(sorted(destination_list, reverse=True))
print("\nstill unsorted:".title())
print(destination_list)


destination_list.reverse()
print("\nreversed list:".title())
print destination_list


destination_list.reverse()
print("\nreversed list to original:".title())
print destination_list


destination_list.sort()
print("\nsorted list:".title())
print destination_list


destination_list.sort(reverse=True)
print("\nsorted list in reverse:".title())
print destination_list
