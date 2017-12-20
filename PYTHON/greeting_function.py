# Practicing Some Python3 Functions


def greet_user():
	"""Display a simple greeting."""
	print("Hello!")

def greet_user(username="<insert name>"):
	"""Display a simple greeting."""
	print("Hello, {0}!".format(username.title()))

def learning_subject():
	"""Display what I am learning"""
	print("I am learning")

def favorite_book(book):
	"""Display what the book I like"""
	print("A book I would like to read is {0}..".format(book.title()))

greet_user()
greet_user('jesse')
learning_subject()
favorite_book('alice in wonderland')

def testing_python_keywords(arg1="arg1",arg2="arg2"):
	"""Testing an occurance of something interesting"""
	print("arg1: " + arg1)
	print("arg2: " + arg2)
	
testing_python_keywords(arg1="arg1",arg2="arg2")
testing_python_keywords()


