# making numberical lists using python3

# range function - 1,2,3,4
# off-by-one python behavior
print("loop with off-by-one behavior - range(1,5):")
for value in range(1, 5):
    print(value)
print("another loop - range(1,6):")

# this should give me - 1,2,3,4,5
for value in range(1, 6):
    print(value)

# making lists
print("making a list with list() and range():")
numbers = list(range(1, 6))
print(numbers)

# more fun with the range operation
print("making a list with the 3rd increment-by value of range():")
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# making square numbers
print("building a sequence of numbers using range:")
squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)
print(squares)

# here is a method of code golf
print("building squares sequence with shortened code:")
squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

# simple statistics in python3
print("using simple statistical methods:")
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print("digits = [1,2,3,4,5,6,7,8,9,0]")
print("min: " + str(min(digits)))
print("max: " + str(max(digits)))
print("sum: " + str(sum(digits)))
