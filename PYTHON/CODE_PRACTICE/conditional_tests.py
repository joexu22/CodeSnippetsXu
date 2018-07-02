# testing conditionals
print("\nSteps towards test driven development:")


car = 'toyota'
print("\nIs car == 'toyota'? I predict True")
print(car == "toyota")
print("\nIs car == 'audi'? I predict False")
print(car == "audi")


joe_car = 'toyota'
mike_car = 'toyota'
print("\nIs joe_car == mike_car? I predict True")
print(joe_car == mike_car)


richard_car = 'lamborghini'
print("\nIs joe_car == richard_car? I predict False (at least for now)")
print(joe_car == richard_car)


common_capitalization = "Government"
common_capitalization_mistake = "government"
print("\nIs common_capitalization == common_capitalization_mistake?; False")
print(common_capitalization == common_capitalization_mistake)
print("\nUsing .lower() on previous equality; True")
print(common_capitalization.lower() == common_capitalization_mistake.lower())


# number conditionals - a.k.a. making of casino games...
print("\nSome random number generation:")
import random
random_int0 = random.randint(1,11)
random_int1 = random.randint(1,11)
random_sum = random_int0 + random_int1
print(str(random_int0) + " + " + str(random_int1) + " = " + str(random_sum))
if random_sum < 11:
	print("low draw")
elif random_sum == 11:
	print("eleven!")
else:
	print("high draw")


# logic gates/truth tables
A = False
B = False
print("\nFalse and False?; False")
print(A and B)
print("\nFalse or False?; False")
print(A or B)

A = False
B = True
print("\nFalse and True?; False")
print(A and B)
print("\nFalse or True?; True")
print(A or B)

A = True
B = False
print("\nTrue and False?; False")
print(A and B)
print("\nTrue or False?; True")
print(A or B)

A = True
B = True
print("\nTrue and True?; True")
print(A and B)
print("\nTrue or True?; True")
print(A or B)


# inclusion tests
online_repo = ["GitHub","GitLab","Bitbucket","Launchpad"]
my_repo = "GitHub"
other_repo = "SourceForge"

if my_repo in online_repo:
	print("\nThis is expected")
if my_repo not in online_repo:
	print("\nThis is not expected")
if other_repo in online_repo:
	print("\nThis is not expected")
if other_repo not in online_repo:
	print("\nThis is expected")
