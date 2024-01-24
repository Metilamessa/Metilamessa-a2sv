class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        ans = 0
        grid = [['' for _ in range(n)] for _ in range(m)]
        left=[[0] * n for _ in range(m)]
        right = [[0] * n for _ in range(m)]  
        up =[[0] * n for _ in range(m)]
        down=[[0] * n for _ in range(m)]
        for row, col in guards:
            grid[row][col] = 'G'

        for row, col in walls:
            grid[row][col] = 'W'

        for i in range(m):
            lastCell = 0
            for j in range(n):
                lastCell = grid[i][j] if grid[i][j] in ('G', 'W') else lastCell
                left[i][j] = lastCell

            lastCell = 0
            for j in range(n - 1, -1, -1):
                lastCell = grid[i][j] if grid[i][j] in ('G', 'W') else lastCell
                right[i][j] = lastCell

        for j in range(n):
            lastCell = 0
            for i in range(m):
                lastCell = grid[i][j] if grid[i][j] in ('G', 'W') else lastCell
                up[i][j] = lastCell

            lastCell = 0
            for i in range(m - 1, -1, -1):
                lastCell = grid[i][j] if grid[i][j] in ('G', 'W') else lastCell
                down[i][j] = lastCell

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '' and left[i][j] != 'G' and right[i][j] != 'G' and up[i][j] != 'G' and down[i][j] != 'G':
                    ans += 1

        return ans
