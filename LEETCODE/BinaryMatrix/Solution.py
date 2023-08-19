from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat or not mat[0]:
            return mat

        m, n = len(mat), len(mat[0])
        queue = []

        # Initialize queue with all cells containing 0s
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = float('inf')

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Breadth First Search
        while queue:
            i, j = queue.pop(0)
            for d in directions:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < m and 0 <= nj < n and mat[ni][nj] > mat[i][j] + 1:
                    mat[ni][nj] = mat[i][j] + 1
                    queue.append((ni, nj))

        return mat