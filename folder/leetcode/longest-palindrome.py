# class Solution:
#     def longestPalindrome(self, s: str) -> int:
#         char_count = {}
#         for char in s:
#             char_count[char] = char_count.get(char, 0) + 1
#         count = 0
#         odd_exist = False
        
#         for value in char_count.values():
#             count += value // 2 * 2
#             if value % 2 != 0:
#                 odd_exists = True
        
#         if odd_exist:
#             count += 1
        
        # return count


class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        count = 0
        odd = False
        
        for value in char_count.values():
            count += value // 2 * 2
            if value % 2 != 0:
                odd = True
        
        if odd:
            count += 1
        
        return count
