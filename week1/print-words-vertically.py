# class Solution:
#     def printVertically(self, s: str) -> List[str]:
#         s = str(input().split)
#         vertical = []

#         for i in s:
#             for j in i:
#                 if s[i][j]:
#                     vertical.append(s[i][j])
#             i+=1

class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()  
        max_length = max(len(word) for word in words)  

        vertical = []
        for i in range(max_length):
            column = ""
            for word in words:
                if i < len(word):
                    column += word[i]
                else:
                    column += " "  
            vertical.append(column.rstrip())  

        return vertical               






        
        