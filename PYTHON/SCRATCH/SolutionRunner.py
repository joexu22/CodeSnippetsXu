# from typing import List
# import collections
# import itertools
# import functools
# import math
# import string
# import random
# import bisect
# import re
# import operator
# import heapq
# import queue

# from queue import PriorityQueue
# from itertools import combinations, permutations
# from functools import lru_cache
# from collections import defaultdict
# from collections import OrderedDict
# from collections import deque
# from collections import Counter

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = dict() #digraph in contingency list 
        for u, v, w in times: graph.setdefault(u, []).append((w, v))
        
        dist = [float("inf")]*N
        
        stack = [(0, K)] #depth-first-search
        while stack: 
            d, n = stack.pop()
            if dist[n-1] <= d: continue
            dist[n-1] = d
            for w, v in sorted(graph.get(n, []), reverse=True): stack.append((d+w, v))
        
        ans = max(dist)
        return ans if ans < float("inf") else -1

print(Solution().networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))
#print(Solution().networkDelayTime([[1,2,1],[2,3,2],[1,3,2]], 3, 1))
#print(Solution().networkDelayTime([[1,2,1],[2,3,2],[1,3,2]], 3, 3))
