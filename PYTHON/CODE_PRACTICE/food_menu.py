# Buffet Menu Code


# main tuple with menu
print("Original Menu:")
food_menu = ("bread","steak","patatoes","salad","cake")
for food in food_menu:
	print(food)


# expected an error here
try:
	food_menu[1] = "fish"
except TypeError:
	print("\nError Expected: individual tuple items cannont be changed")


# replaced the entire tuple
print("\nChanged Menu:")
food_menu = ("chips","fish","patatoes","salad","cake")
for food in food_menu:
	print(food)
