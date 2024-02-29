class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def maxScore(left, right, turn):
            if left > right:
                return 0
            if turn:
                option1 = nums[left] + maxScore(left + 1, right, not turn)
                option2 = nums[right] + maxScore(left, right - 1, not turn)
                return max(option1, option2)
            
            else:
                option1 = -nums[left] + maxScore(left + 1, right, not turn)
                option2 = -nums[right] + maxScore(left, right - 1, not turn)
                return min(option1, option2)
        
        score = maxScore(0, len(nums) - 1, True)
        return score >= 0
