class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = {}
        cur_sum = 0
        count = 0

        for num in nums:
            cur_sum += num
            if cur_sum == k:
                count += 1
            if cur_sum - k in prefix_sum:
                count += prefix_sum[cur_sum - k]
            prefix_sum[cur_sum] = prefix_sum.get(cur_sum, 0) + 1

        return count

