a = [5,2,4,6,1,3]
b = [3,2]

def IS(array):
    for j in range (1,len(array)):
        key = array[j]
        i = j - 1
        while (i >= 0 and array[i] > key):
            array[i + 1] = array[i]
            i = i - 1
        array[i+1] = key
    return array

print(IS(b))
print(IS(a))
