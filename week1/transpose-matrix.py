class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])
        transpose = [[0] * n for _ in range(m)]

        for row in range(n):
            for col in range(m):
                transpose[col][row] = matrix[row][col]

        return transpose