class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        suffix_sum = [0] * (n + 1)
        
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]
        
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + nums[i]
        result = []
        
        for i in range(n):
            left_sum = nums[i] * i - prefix_sum[i]
            right_sum = suffix_sum[i + 1] - nums[i] * (n - i - 1)
            result.append(left_sum + right_sum)
        
        return result
