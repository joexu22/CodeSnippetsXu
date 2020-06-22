import sys

A = [1,4,2,3,5,8,9,4]

def function_sort(A):
    return 0;

def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j -1
        while (i >= 0 and A[i] > key):
            A[i+1] = A[i]
            i = i - 1
        A[i + 1] = key
    return A

print(A)
print(insertion_sort(A))