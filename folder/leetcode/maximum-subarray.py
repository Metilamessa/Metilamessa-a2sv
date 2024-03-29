class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        ans = nums[0]

        pre = 0

        for num in nums:
            pre += num
            ans = max(pre, ans)
            if pre < 0:
                pre = 0
        return ans            