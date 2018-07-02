# Excersize on List Comprehensions
# personally consider this an excersize in code golf
print("list comprehension:".title())

print("squares = [value**2 for value in range(1,11)]")
squares = [value**2 for value in range(1, 11)]
print(squares)

# counting excersize
print("counting from 1 to 20 inclusive")
for value in range(1, 21):
    print(value)

print("couting from 1 to a million inclusive")
# takes a bit but works fine
# for value in range(1,10**6+1):
#	print(value)

print("summing a million")
million_array = [value for value in range(1, 10**6 + 1)]
print("checking min: " + str(min(million_array)))
print("checking max: " + str(max(million_array)))
print("checking sum: " + str(sum(million_array)))

print("making a list of odd number from 1 to 20")
for value in range(1, 21, 2):
    print value

print("making a list of multiples of 3 from 3 to 30")
for value in range(3, 31, 3):
    print value

print("making a list of cubes from 1 to 10")
cubes = []
for value in range(1, 11):
    cubes.append(value**3)
for cube in cubes:
    print cube

print("making a list of cubes from 1 to 10 with list comprehension")
cubes = [value**3 for value in range(1, 11)]
for cube in cubes:
    print cube
