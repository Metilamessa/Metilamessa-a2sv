class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def is_nice(sub):
            for ch in sub:
                if ch.lower() not in sub or ch.upper() not in sub:
                    return False
            return True

        longest_substring = ""
        n = len(s)

        for i in range(n):
            for j in range(i + 1, n + 1):
                substring = s[i:j]
                if is_nice(substring) and len(substring) > len(longest_substring):
                    longest_substring = substring

        return longest_substring