class Solution:
    def isPalindrome(self, s: str) -> bool:        
        s = s.lower()
        strings = [char for char in s if char.isalnum()]       
              
        left = 0
        right = len(strings)-1
        while left < right:
            if strings[left] != strings[right]:
                return False  
            left += 1
            right -= 1

        return True 

