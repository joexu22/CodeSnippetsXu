A = [6,8,5,3,9,2,1,7,0,7,4]
def insertion_sort(Array):
    for i in range(1,len(A)):
        key = A[i]
        j = i - 1
        while (j>=0 and A[j]>key):
            A[j+1] = A[j]
            j = j - 1
        A[j+1] = key
    return A

print(insertion_sort(A))