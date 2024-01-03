class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        num = 1

        for i in range(n - 1, -1, -1):
            digits[i] += num
            
            if digits[i] < 10:
                num = 0
                break
            
            digits[i] = 0

        if num == 1:
            digits.insert(0, 1)

        return digits
            