# Python3 excersize involving the use of T-Shirt

def make_shirt(size="medium", message="I love Python"):
	print("Your shirt is size: " + size)
	print("The message on your shirt is: " +  message)

make_shirt("medium", "Hello, World!")

# making sure positional arguments are equivalent
make_shirt(message="This is a Shirt!", size="large")
make_shirt(size="large", message="This is a Shirt!")

make_shirt()

make_shirt(size="small")
