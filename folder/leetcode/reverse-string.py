class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        def rev(left, right):
            if left >= right:
                return 
                     
            s[left], s[right] = s[right], s[left]
            return rev(left + 1, right - 1)
        left = 0
        right = len(s) - 1
        rev(left, right)
        
    
    
