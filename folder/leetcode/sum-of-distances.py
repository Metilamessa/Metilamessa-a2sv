class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        left_sum = defaultdict(int)
        count_left = defaultdict(int)
        
        for i, j in enumerate(nums):
            res[i] += count_left[j] * i
            res[i] -= left_sum[j]
            count_left[j] += 1
            left_sum[j] += i
        
        right_sum = defaultdict(int)
        count_right = defaultdict(int)
        for i, j in reversed(list(enumerate(nums))):
            res[i] += right_sum[j]
            res[i] -= count_right[j] * i

            count_right[j] += 1
            right_sum[j] += i

        return res    
        
        
       