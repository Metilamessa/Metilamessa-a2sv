class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        output = float('inf')  
        window_sum = 0

        while right < len(nums):
            window_sum += nums[right]

            while window_sum >= target:
                output = min(output, right - left + 1)
                window_sum -= nums[left]
                left += 1

            right += 1

        return output if output != float('inf') else 0 
