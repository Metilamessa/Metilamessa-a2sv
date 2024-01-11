class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count_zero = 0
        max_len = 0
        left = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                count_zero += 1
            while count_zero > 1:
                if nums[left] == 1:
                    left += 1
                else:
                    count_zero -= 1
                    left += 1

            max_len = max(max_len, right - left + 1 - count_zero)
        if sum(nums) == len(nums):
            return max_len-1
            
        return max_len