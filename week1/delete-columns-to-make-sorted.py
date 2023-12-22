class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        col_deleted = 0       
        for str in range(len(strs[0])):
            for i in range(1, len(strs)):
                if strs[i][str] < strs[i-1][str]:
                    col_deleted += 1
                    break
        return col_deleted


 
       