class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()  
        max_num = 0  

        for cost in costs:
            if coins >= cost:
                coins -= cost
                max_num += 1
            else:
                break

        return max_num