# An excersize related to foods
joes_foods = ["rice", "pork intestine wraped in cornmeal",
              "pumpkin buscuit", "cloud ear fungus"]
mikes_foods = joes_foods[:]


# testing to make sure the "copy" worked
print(joes_foods)
print(mikes_foods)


# making sure the two lists are different
print("\ntesting that the two lists are indeed different:")
joes_foods.append("pinapple")
mikes_foods.append("orange juice")
print(joes_foods)
print(mikes_foods)
