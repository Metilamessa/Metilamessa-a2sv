class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        Array = []
        i=0
        while i < len(nums):
            sum += nums[i]
            Array.append(sum)
            i += 1
        return Array