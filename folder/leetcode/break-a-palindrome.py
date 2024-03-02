class Solution:
    def breakPalindrome(self, palindrome: str) -> str:




        if len(palindrome) == 1:
            return ""
        
        for i in range(len(palindrome)):
            if palindrome[i] != "a":
                newStr = palindrome[:i] +"a"+ palindrome[i + 1:]

                if newStr == newStr[:: -1]:
                    return palindrome[:-1] + "b"
                return newStr
        return palindrome[:-1] + "b"        