class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        start = 0
        charIndexMap = {}

        for i, char in enumerate(s):
            if char in charIndexMap and charIndexMap[char] >= start:
                start = charIndexMap[char] + 1

            maxLength = max(maxLength, i - start + 1)
            charIndexMap[char] = i

        return maxLength