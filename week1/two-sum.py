class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ind_nums = {}

        for i, num in enumerate(nums):
            
            another_num = target - num
            if another_num in ind_nums:
                return [i, ind_nums[another_num]]           
            ind_nums[num] = i
        