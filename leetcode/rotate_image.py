from typing import List
class Solution:
    def rotate_sides(self, matrix: List[List[int]]) -> None:
        N = len(matrix)
        if N == 1:
            return

        start = 0
        end = N
        while N > 1:
            elems = [0 for _ in range(4*N-4)]
            index = 0
            for c in range(start, end):
                elems[(index + N - 1) % (4*N-4)] = matrix[start][c]
                index += 1
            for r in range(start + 1, end):
                elems[(index + N - 1) % (4*N-4)] = matrix[r][end-1]
                index += 1
            for c in range(end - 2, start, -1):
                elems[(index + N - 1) % (4*N-4)] = matrix[end - 1][c]
                index += 1
            for r in range(end - 1, start, -1):
                elems[(index + N - 1) % (4*N-4)] = matrix[r][start]
                index += 1

            index = 0
            for c in range(start, end):
                matrix[start][c] = elems[index]
                index += 1
            for r in range(start + 1, end):
                matrix[r][end-1] = elems[index]
                index += 1
            for c in range(end - 2, start, -1):
                matrix[end - 1][c] = elems[index]
                index += 1
            for r in range(end - 1, start, -1):
                matrix[r][start] = elems[index]
                index += 1

            start += 1
            end -= 1
            N -= 2

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.rotate_sides(matrix)
        return matrix

print(Solution().rotate([[4, 8], [3, 6]]))
print(Solution().rotate([[1,2,3],[4,5,6],[7,8,9]]))
print(Solution().rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))
