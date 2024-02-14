class Solution:
    def minimumSteps(self, s: str) -> int:
        
        steps = 0
        zeros_encountered = 0
        
        for i in range(len(s)):
            if s[i] == '0':
                steps += i - zeros_encountered
                zeros_encountered += 1
        
        return steps

        