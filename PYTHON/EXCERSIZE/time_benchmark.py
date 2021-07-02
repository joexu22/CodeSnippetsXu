from timeit import timeit

"""
This is a short introduction to the timeit module
Also, I am benchmarking ways to create lists in Python
"""

# Test 1
test = """
my_list = []
for i in range(50):
    my_list.append(0)
"""

print(timeit(test))

# Test 2
test = """
my_list = []
for i in range(50):
    my_list += [0]
"""
print(timeit(test))

# Test 3
test = "my_list = [0 for i in range(50)]"
print(timeit(test))

# Test 4
test = "my_list = [0] * 50"
print(timeit(test))
