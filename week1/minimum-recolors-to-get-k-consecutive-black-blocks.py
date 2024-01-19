class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        operations = 0

        for i in range(k):
            if blocks[i] == 'W':
                operations += 1
        min_operations = operations

        for i in range(k, n):
            if blocks[i - k] == 'W':
                operations -= 1
            if blocks[i] == 'W':
                operations += 1
            min_operations = min(min_operations, operations)

        return min_operations

