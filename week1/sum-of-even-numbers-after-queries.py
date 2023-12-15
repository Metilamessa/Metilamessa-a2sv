class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        result = []
        even_sum = sum(num for num in nums if num % 2 == 0)

        for val, index in queries:
            old_num = nums[index]
            nums[index] += val
            new_num = nums[index]

            if old_num % 2 == 0:
                even_sum -= old_num

            if new_num % 2 == 0:
                even_sum += new_num

            result.append(even_sum)

        return result
        
        