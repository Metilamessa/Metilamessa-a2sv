class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num)
        i = n - 1

        while i >= 0:
            if int(num[i]) % 2 == 1:
                return num[:i+1]
            i -= 1

        return ""
        