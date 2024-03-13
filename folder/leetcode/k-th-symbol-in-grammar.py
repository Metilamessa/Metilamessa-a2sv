class Solution:
    def kthGrammar(self, n: int, k: int) -> int:

        if n == 1:
            return 0

        parent_k = (k + 1) // 2
        parent_symbol = self.kthGrammar(n - 1, parent_k)

        if parent_symbol == 0:
            if k % 2 == 1:
                return 0
            else:
                return 1
        else:
            if k % 2 == 1:
                return 1
            else:
                return 0   

    