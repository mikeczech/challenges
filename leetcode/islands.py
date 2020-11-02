from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        N = len(grid)
        M = len(grid[0])
        visited = set()
        res = 0

        for r in range(N):
            for c in range(M):
                if grid[r][c] == "1" and (r, c) not in visited:
                    res += 1 
                    queue = deque([(r, c)])
                    while queue:
                        next_r, next_c = queue.popleft()
                        if grid[next_r][next_c] == "1" and (next_r, next_c) not in visited:
                            visited.add((next_r, next_c))
                            if next_r + 1 < N:
                                queue.append((next_r+1, next_c))
                            if next_c + 1 < M:
                                queue.append((next_r, next_c+1))
                            if next_r - 1 >= 0:
                                queue.append((next_r-1, next_c))
                            if next_c - 1 >= 0:
                                queue.append((next_r, next_c-1))
        return res

assert Solution().numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]) == 3
