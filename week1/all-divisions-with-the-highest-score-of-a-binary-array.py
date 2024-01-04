class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        max_score = float('-inf')
        result = []

        zeros = nums.count(0)
        ones = nums.count(1)

        nums_left_zeros = 0
        nums_right_ones = ones

        for i in range(n + 1):
            score = nums_left_zeros + nums_right_ones

            if score > max_score:
                max_score = score
                result = [i]
            elif score == max_score:
                result.append(i)

            if i < n:
                if nums[i] == 0:
                    nums_left_zeros += 1
                else:
                    nums_right_ones -= 1

        return result