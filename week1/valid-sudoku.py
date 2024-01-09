class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
            
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [[set() for _ in range(3)] for _ in range(3)]

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num != '.':
                    if num in rows[r] or num in columns[c] or num in boxes[r//3][c//3]:
                        return False
                    rows[r].add(num)
                    columns[c].add(num)
                    boxes[r//3][c//3].add(num)

        return True