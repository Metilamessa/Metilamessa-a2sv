class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:


        pre_sum = 0
        ans = 0

        for i, num in enumerate(nums):
            pre_sum += num
            ans = max(ans, (-1)*(-pre_sum//(i+1)))
        return ans
        
        