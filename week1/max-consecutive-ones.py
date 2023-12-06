# class Solution:
#     def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
#         ans = 0
#         count +=1
#         for i in nums:
#             for j in range(i+1,len(nums))
#                 if num[i] = num[j]
#                 ans += 1
                
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        count = 0
        for i in nums:
            if i == 1:
                count += 1
                ans = max(ans, count)
            else:
                count = 0
        return ans       