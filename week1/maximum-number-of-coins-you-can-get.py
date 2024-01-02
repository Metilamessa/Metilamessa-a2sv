class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        coins = 0
        piles.sort()
        for i in range(len(piles)//3):
            coins += piles[-2 - 2*i]
        
        return coins
        