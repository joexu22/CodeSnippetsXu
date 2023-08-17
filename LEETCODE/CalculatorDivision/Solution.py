from collections import defaultdict
from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def dfs(start, end, path, visited):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return path
            visited.add(start)

            for neighbor, value in graph[start]:
                if neighbor not in visited:
                    result = dfs(neighbor, end, path * value, visited)
                    if result != -1.0:
                        return result

            return -1.0

        graph = defaultdict(list)
        for (a, b), value in zip(equations, values):
            graph[a].append((b, value))
            graph[b].append((a, 1 / value))

        result = []
        for a, b in queries:
            result.append(dfs(a, b, 1, set()))

        return result