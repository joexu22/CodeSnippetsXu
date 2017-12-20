# Python excersizes to warm myself up
# Demonstration of Python3 skills

# making of a really interesting party
guest_list = ["Jesus", "Hitler", "Shakespeare", "Muhammad", "Washington"]
print("I would like to cordially invite you " + guest_list[0] + " to dinner")
print("I would like to cordially invite you " + guest_list[1] + " to dinner")
print("I would like to cordially invite you " + guest_list[2] + " to dinner")
print("I would like to cordially invite you " + guest_list[3] + " to dinner")
print("I would like to cordially invite you " + guest_list[4] + " to dinner")

# Washington can't make it, replace with Lincon
print(guest_list[4] + " is not able to make it to the party")
guest_list.remove("Washington")
guest_list.insert(4, "Lincon")

print("\nnew invatations:".title())
print("I would like to cordially invite you " + guest_list[0] + " to dinner")
print("I would like to cordially invite you " + guest_list[1] + " to dinner")
print("I would like to cordially invite you " + guest_list[2] + " to dinner")
print("I would like to cordially invite you " + guest_list[3] + " to dinner")
print("I would like to cordially invite you " + guest_list[4] + " to dinner")

# Inviting 3 more guests
guest_list.insert(0, "Teresa")
guest_list.insert(3, "Gandhi")
guest_list.append("Einstein")

print("\nnew invatations - bigger table:".title())
print("I would like to cordially invite you " + guest_list[0] + " to dinner")
print("I would like to cordially invite you " + guest_list[1] + " to dinner")
print("I would like to cordially invite you " + guest_list[2] + " to dinner")
print("I would like to cordially invite you " + guest_list[3] + " to dinner")
print("I would like to cordially invite you " + guest_list[4] + " to dinner")
print("I would like to cordially invite you " + guest_list[5] + " to dinner")
print("I would like to cordially invite you " + guest_list[6] + " to dinner")
print("I would like to cordially invite you " + guest_list[7] + " to dinner")
