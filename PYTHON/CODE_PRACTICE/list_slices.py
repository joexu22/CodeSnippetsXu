# Python3 list slices
# remembering 0 based counting and 1 based counting is a real skill

# the list to work with
players = ["charles", "martina", "michael", "florence", "eli"]
print('players = ["charles","martina","michael","florence","eli"]')

# understanding [0:3] slice
print("\nthe 1st, 2nd, and 3rd person - players[0:3]")
print(players[0:3])

# understanding [1:4] slice
print("\nthe 2st, 3nd, and 4th person - players[1:4]")
print(players[1:4])
print(players[1:-1])

# understanding [:4] slice
print("\nstart slicing from the beginning - player[:4]")
print("expecting the 1st, 2nd, 3rd, and 4th item")
print(players[:4])

# testing logical issue with loop notation and slice notation
print("\n logical bug:".title())
test_numbers = []
for i in range(0, 5):
    test_numbers.append(i)
print(test_numbers)
print(test_numbers[0:5])
print("so the logic actually checks out...")

# understanding the [2:] slice
print("\nstart slicing to the end - player[2:]")
print("expecting the 3rd, 4th, and 5th item")
print(players[2:])


# understanding negative notation
print("\nusing negative slices - player[-3:]")
# [ 0,  1,  2,  3,  4]
# [-5, -4, -3, -2, -1]
print("expecting the 3rd, 4th, and 5th item")
print(players[-3:])
print(players[2:])

# using slices in excersize
print("\nprinting the first 3 slices")
for player in players[:3]:
    print player

print("\nprinting 3 items from the middle")
for player in players[1:4]:
    print player

print("\nprinting last 3 items")
for player in players[-3:]:
    print player
