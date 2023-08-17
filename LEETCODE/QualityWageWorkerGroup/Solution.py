class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = sorted(zip(quality, wage), key=lambda x: x[1] / x[0])
        min_cost = float('inf')
        quality_sum = 0
        quality_heap = []

        for q, w in workers:
            heapq.heappush(quality_heap, -q)
            quality_sum += q

            if len(quality_heap) > k:
                quality_sum += heapq.heappop(quality_heap)

            if len(quality_heap) == k:
                min_cost = min(min_cost, quality_sum * w / q)

        return min_cost