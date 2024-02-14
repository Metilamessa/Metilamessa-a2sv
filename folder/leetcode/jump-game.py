class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        k = len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if i+nums[i]>=k:
                k = i
            else:
                i -= 1
        return True if k == 0  else False
            
                
            
        