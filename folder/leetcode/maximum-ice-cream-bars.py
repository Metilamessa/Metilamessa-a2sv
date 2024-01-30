class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        mux_num = 0

        for cost in costs:
            if coins >= cost:
                coins -= cost
                mux_num += 1
            else:
                break

        return mux_num
