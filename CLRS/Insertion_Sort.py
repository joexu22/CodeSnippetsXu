"""
Insertion Sort Code
Specifially paying attention to the concept of "Loop Invariants"
"Mathmatics" involving the accuracy and provability of code
"""

# Regular Insertion Sort
def ins_sort(array):
    for j in range(1,len(array)):
        key = array[j]
        i = j - 1
        while i>=0 and array[i]>key:
            array[i + 1] = array[i]
            i = i - 1
        array[i + 1] = key
        print(array)
    return array

# Insertion Sort but Reversed
def rev_ins(array):
    for j in range(1,len(array)):
        key = array[j]
        i = j - 1
        while i>=0 and array[i]<key:
            array[i + 1] = array[i]
            i = i - 1
        array[i + 1] = key
        print(array)
    return array

# Sample Problem
# I should use some notion of Test Driven Development
A = [5,2,4,6,1,3]
ins_sort(A)
rev_ins(A)