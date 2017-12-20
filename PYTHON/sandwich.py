# very, very simple sandwich function

def make_sandwich(*ingredients):
	"""printing out a sandwich"""
	print("\nCreating a sandwich with the following ingredients:")
	for item in ingredients:
		print(" -" + item)

make_sandwich("olive","avocado","peppers","apple",)
make_sandwich("pesto","apple",)
make_sandwich("slaw","mint","pear",)
