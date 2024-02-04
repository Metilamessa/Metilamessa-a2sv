class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        visited = {}
        maximum = 0
        result = 0
        l=0

        for i, n in enumerate(nums):
            if n in visited:
                while l < visited[n]+1:
                    maximum -= nums[l]
                    l+=1
            visited[n] = i
            maximum +=n
            result = max(result,maximum)
        return result