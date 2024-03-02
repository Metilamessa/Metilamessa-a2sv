class Solution:
    def numberOfWays(self, s: str) -> int:
        prefix = []
        count_one = count_zero = 0
        for c in s:                                
            prefix.append([count_zero, count_one])
            if c == '1':
                count_one += 1
            else:
                count_zero += 1    
        
        suffix = []        
        count_one = count_zero = 0
        for c in s[::-1]:                          
            suffix.append([count_zero, count_one])
            if c == '1':
                count_one += 1
            else:
                count_zero += 1    
        
        suffix = suffix[::-1]                      
        result = 0
        for i, c in enumerate(s):                  
            if c == '1':
                result += prefix[i][0] * suffix[i][0]
            else:    
                result += prefix[i][1] * suffix[i][1]
        
        return result