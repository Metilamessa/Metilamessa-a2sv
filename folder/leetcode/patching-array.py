class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        covered = 0
        patch = 0
        i = 0

        while covered < n:
            if i < len(nums) and nums[i] <= covered + 1:
                covered += nums[i]
                i += 1
            else:
                covered += covered + 1
                patch += 1

                if covered >= n:
                    break

        return patch

    


 







 
    
        
        









