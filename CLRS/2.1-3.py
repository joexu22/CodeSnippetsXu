"""
Linear Search with loop invariants
"""

def linear_search(array, v):
    i = None
    for j in range(0,len(array)):
        if v == array[j]:
            i = j
            return i
    return i

A = [5,2,4,6,1,3]
print(linear_search(A,3))
print(linear_search(A,7))

