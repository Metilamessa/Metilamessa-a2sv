class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        cur_index = 0
        n = len(nums)
        while cur_index < n:
            if nums[cur_index] != val:
                nums[i] = nums[cur_index]
                i += 1

            cur_index += 1
        return i