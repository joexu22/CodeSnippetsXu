class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        if not roads:
            return 0

        graph = defaultdict(set)
        for road in roads:
            graph[road[0]].add(road[1])
            graph[road[1]].add(road[0])

        max_rank = 0
        for i in range(n):
            for j in range(i + 1, n):
                rank = len(graph[i]) + len(graph[j])
                if i in graph[j]:
                    rank -= 1
                max_rank = max(max_rank, rank)

        return max_rank