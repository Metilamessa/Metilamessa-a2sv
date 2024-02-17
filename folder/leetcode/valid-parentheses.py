class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in "[({":
                stack.append(i)
            else:
                if not stack:
                    return False
                last = stack.pop()
                togeth = last + i
                if togeth != "()" and togeth != "[]" and togeth != "{}":
                    return False
                
        return not stack