def InsertionSort(array):
    
    for i in range(0, len(array)):
        temp = array[i]
        index = i - 1
        while array[index] > temp and index >= 0:
            array[index + 1] = array[index]
            index -= 1
        array[index + 1] = temp
    return array

print(InsertionSort([10,9,8,7,6,5,4,3,2,1]))
