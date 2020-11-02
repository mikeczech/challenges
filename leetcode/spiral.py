from typing import List

class Solution:
    def print_spiral(self, matrix: List[List[int]], res) -> List[int]:
        N = len(matrix)
        if N < 1:
            return
        M = len(matrix[0])

        if N == 1:
            for c in range(0, M):
                res.append(matrix[0][c])
        elif M == 1:
            for r in range(0, N):
                res.append(matrix[r][0])
        else:
            for c in range(0, M):
                res.append(matrix[0][c])
            for r in range(1, N):
                res.append(matrix[r][M - 1])
            for c in range(M - 2, 0, -1):
                res.append(matrix[N - 1][c])
            for r in range(N - 1, 0, -1):
                res.append(matrix[r][0])

        if N > 2 and M > 2:
            next_matrix = [m[1:M-1] for m in matrix[1:N-1]]
            self.print_spiral(next_matrix, res)

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        self.print_spiral(matrix, res)
        return res

print(Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
print(Solution().spiralOrder([[3],[2]]))
print(Solution().spiralOrder([[1,11],[2,12],[3,13],[4,14]]))
