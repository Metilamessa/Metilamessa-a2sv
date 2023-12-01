class Solution:
    def sumOfThree(self, num: int) -> List[int]:
       
        max_middle = num // 3  
        for middle in range(max_middle - 1, max_middle + 2):
            start = middle - 1
            end = middle + 1
            if start + middle + end == num:
                return [start, middle, end]
        return [] 