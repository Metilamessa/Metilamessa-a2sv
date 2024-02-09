class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        m = len(s)
        res = [0]*(m+1)
        for start, end, direction in shifts:
            if direction == 1:
                res[start]+=1
                res[end+1]-=1 
            else:
                res[start]-=1
                res[end+1]+=1
        res.pop()
        for i in range(1,len(s)):
            res[i]+=res[i-1]
        ans=[]
        order_a = ord('a')
        for i, n in enumerate(s):
            char1=(ord(n)-order_a+res[i])%26
            ans.append(chr(char1 + order_a))
        return "".join(ans)

