"""
Write a function that, given an array A of N integers, returns the lagest integer K > 0 such that both values K and -K exist in array A. If there is no such integer, the function should return 0.

Example 1:

Input: [3, 2, -2, 5, -3]
Output: 3
Example 2:

Input: [1, 2, 3, -4]
Output: 0
"""
input1 = [3, 2, -2, 5, -3]
input2 = [1, 2, 3, -4]

largestK = 0
pos_neg_table = {}
for i in input2:
    if i in pos_neg_table:
        if abs(i) > largestK:
            largestK = abs(i)
    else:
        pos_neg_table[i] = True
        pos_neg_table[-i] = True

print(largestK)
print(pos_neg_table)

