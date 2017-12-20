# code that makes pizzas
import pizza
import pizza as p
from pizza import make_pizza
from pizza import make_pizza as mp
from pizza import *  # import all functions

# importing whole file
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# importing whole file with an alias
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# importing the specific file
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# importing the specific file with an alias
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
