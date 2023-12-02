class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:
            return ""
   
        min_length = min(len(s) for s in strs)
        strs.sort()
        for i in range(min_length):
        
            if any(s[i] != strs[0][i] for s in strs):
            
                return strs[0][:i]

        return strs[0]


    