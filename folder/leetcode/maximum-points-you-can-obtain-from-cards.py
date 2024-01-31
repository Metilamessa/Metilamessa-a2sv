class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total_sum = sum(cardPoints)
        window_sum = sum(cardPoints[:n - k])
        max_score = total_sum - window_sum

        for i in range(k):
            window_sum -= cardPoints[i]
            window_sum += cardPoints[i + n - k]
            max_score = max(max_score, total_sum - window_sum)

        return max_score
