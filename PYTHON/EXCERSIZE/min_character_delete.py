def minCntCharDeletionsfrequency(str, N):
    charMap = {}
    charCount = []
    charSet = set()
    delCount = 0

    for i in range(len(str)):
        charMap[str[i]] = charMap.get(str[i], 0) + 1

    print(charMap)

    for key in charMap:
        charCount.append(charMap[key])

    print(charCount)

    for i in charCount:
        if i not in charSet:
            charSet.add(i)
        else:
            while i in charSet and i > 0:
                i -= 1
                delCount += 1
        charSet.add(i)
    return delCount

 
# Driver Code
if __name__ == '__main__':
     
    str = "abbccccddddeeee"
 
    # Stores length of str
    N = len(str)
     
    print(minCntCharDeletionsfrequency(str, N))
 
# This code is contributed by mohit kumar 29