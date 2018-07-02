# a python3 excersize on loops and lists

magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(magician)

print("\napplaud each magician:".title())
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Thank you, everyone. That was a great magic show!")

# excersize on pizza toppings
pizza_toppings = ["pepperoni", "cheese", "mushroom"]
print("\nmy favorite pizza toppings:".title())
for topping in pizza_toppings:
    print("I like " + topping + " pizza.")
print("I really like pizza!")

# excersize on favorite animals
animals = ["wolf", "snake", "fox"]
print("\nmy favorite animals:".title())
for animal in animals:
    print("A " + animal + " would make a great pet.")
print("Any of these animals would make for a great pet")
