class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        count_p = Counter(p)
        count_window = Counter(s[:len(p)])
        required = len(p)

        for right in range(len(p), len(s)):
            if count_window == count_p:
                ans.append(right - len(p))

            count_window[s[right]] += 1
            count_window[s[right - len(p)]] -= 1

            if count_window[s[right - len(p)]] == 0:
                del count_window[s[right - len(p)]]

        if count_window == count_p:
            ans.append(len(s) - len(p))

        return ans
