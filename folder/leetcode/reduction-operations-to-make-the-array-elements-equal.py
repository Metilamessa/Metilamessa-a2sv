class Solution:
    def reductionOperations(self, nums: List[int]) -> int :    
        no_opration = 0
        nums.sort()

        for i in range(len(nums) - 1, 0, -1):
            if nums[i] != nums[i - 1]:
                no_opration += len(nums) - i

        return no_opration