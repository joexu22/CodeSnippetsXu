# mountain_poll.py
# dictionary filling technique that might be really useful


# dictionary being created
responses = {}

# flag
polling_active = True

while polling_active:
	# Prompt for the person's name and response.
	name = input("\nWhat is your name? ")
	response = input("Which mountain would you like to climb someday? ")
	
	responses[name] = response
	
	repeat = input("Would you like to let another person respond? (y/n) ")
	if repeat == "n":
		polling_active = False

print("\n--- Poll Result ---")
for name, response in responses.items():
	print(name + " would like to climb "+ response + ".")
