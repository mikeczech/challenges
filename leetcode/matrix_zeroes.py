class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 0:
                    for c in range(len(matrix[row])):
                        if matrix[row][c] != 0:
                            matrix[row][c] = None
                    for r in range(len(matrix)):
                        if matrix[r][col] != 0:
                            matrix[r][col] = None

        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if not matrix[row][col]:
                    matrix[row][col] = 0

        return matrix
