# Taking in user input, parroting


# easy application of input()
prompt = "\nTell me something, and I will parrot back your message: "
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
	message = input(prompt)
	if message == 'quit':
		active = False
	else:
		print(message)
