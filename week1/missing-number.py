class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum_with_missing = (n * (n + 1)) // 2  
        actual_sum = sum(nums)  

        return sum_with_missing - actual_sum 
        