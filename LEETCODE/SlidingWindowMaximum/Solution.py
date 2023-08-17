from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        def clean_deque(i):
            if deq and deq[0] == i - k:
                deq.popleft()
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()

        deq = deque()
        max_idx = 0
        for i in range(k):
            clean_deque(i)
            deq.append(i)
            if nums[i] > nums[max_idx]:
                max_idx = i
        output = [nums[max_idx]]

        for i in range(k, len(nums)):
            clean_deque(i)
            deq.append(i)
            output.append(nums[deq[0]])

        return output