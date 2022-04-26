"""
Input: piles = [5, 2, 1]
Output: 3
Explanation:
Step 1: reducing 5 -> 2 [2, 2, 1]
Step 2: reducing 2 -> 1 [2, 1, 1]
Step 3: reducing 2 -> 1 [1, 1, 1]
So final number of steps required is 3.
"""


array = [1,2,3]
pile = sorted(array, reverse=True)
print(pile)

array2 = [1, 1, 2, 2, 2, 3, 3, 3, 4, 4]
array2.sort(reverse=True)
print(array2)

count = 0
current_pile = array2[0]
for i in range(len(array2)):
    if current_pile != array2[i]:
        count += i
        current_pile = array2[i]

print(count)
#if array[3]:
#    print("out");
#else:
#    print("in"); 