class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        left = 0 
        right = 0
        max_len = 0



        while right < len(s):
            if s[right] not in substring:
                substring.add(s[right])
                max_len = max(max_len,right-left+1)
                right += 1
            else:
                substring.remove(s[left])
                left += 1
        return max_len