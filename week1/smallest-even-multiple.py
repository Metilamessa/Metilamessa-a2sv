class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        m = n
        k = n*2
        if m %2 ==0:
            return m
        else:
            return k