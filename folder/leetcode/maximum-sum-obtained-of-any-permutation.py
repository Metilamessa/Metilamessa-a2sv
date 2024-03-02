class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:





        length = len(nums)
        req_length = len(requests)
        freq_list = [0 for _ in range(length)]    
        
        for i in range(req_length):
            freq_list[requests[i][0]] += 1
            if requests[i][1] < length - 1:
                freq_list[requests[i][1] + 1] -= 1
        
        for i in range(length):
            if i == 0:
                continue
            freq_list[i] += freq_list[i - 1]

        freq_list.sort()
        nums.sort()
        result = 0
        MOD = int(1e9 + 7)
        
        for i in range(length - 1, -1, -1):
            result += (freq_list[i] * nums[i]) % MOD
            result %= MOD
        
        return int(result % MOD)
        