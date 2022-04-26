"""
Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.

Return the maximum possible length of s.

Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.

Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible solutions are "chaers" and "acters".

Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
"""

from itertools import combinations

arr = ["cha","r","act","ers"]
total_comb = []
for i in range(len(arr)+1):
    comb = combinations(arr, i)
    for j in comb:
        total_comb.append(j)
print(total_comb)

string_arr = []
for comb in total_comb:
    string = ""
    for chars in comb:
        string += chars
    string_arr.append(string)

def isUnique(string):
    chars = set()
    for char in string:
        if char in chars:
            return False
        else:
            chars.add(char)
    return True

maxLength = 0
for i in string_arr:
    if isUnique(i) and len(i)>maxLength:
        maxLength = len(i)

print(maxLength)