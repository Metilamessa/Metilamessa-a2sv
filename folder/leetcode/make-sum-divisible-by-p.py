class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
    
        target = sum(nums) % p
        if target == 0:
            return 0
        
        n = len(nums)
        prefix_sum = 0
        prefix_sums = {0: -1}
        min_length = float('inf')
        
        for i in range(n):
            prefix_sum = (prefix_sum + nums[i]) % p
            complement = (prefix_sum - target) % p
            
            if complement in prefix_sums:
                min_length = min(min_length, i - prefix_sums[complement])
            
            prefix_sums[prefix_sum] = i
        
        if min_length == n or min_length == float('inf'):
            return -1
        else:
            return min_length

        


        