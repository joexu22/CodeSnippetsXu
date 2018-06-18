# code concerning tuples
"""
Tuples are data objects that one does not expect to change throught the
lifetime of a product.
"""

# sample tuple
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])


# changing a tuple will raise an error
# dimensions[0] = 250  # bad code


# accessing tuples
for dimension in dimensions:
	print(dimension)


# ability to overwrite the entire tuple
print("\nOriginal Dimensions:")
for dimension in dimensions:
	print(str(dimension))


# modified dimensions
dimensions = (400,100)
print("\nModified Dimensions:")
for dimension in dimensions:
	print(str(dimension))
