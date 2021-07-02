def zeno_cost(d, c, f):
    cost = 0
    cost += zeno_cost(d/2)
    return cost

print(zeno_cost(128, 2, .5))
