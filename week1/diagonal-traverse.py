class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []

        m, n = len(mat), len(mat[0])
        result = []

        for d in range(m + n - 1):
            if d % 2 == 0:  
                for i in range(min(d, m - 1), max(0, d - n + 1) - 1, -1):
                    result.append(mat[i][d - i])
            else:  
                for i in range(max(0, d - n + 1), min(d, m - 1) + 1):
                    result.append(mat[i][d - i])

        return result
        