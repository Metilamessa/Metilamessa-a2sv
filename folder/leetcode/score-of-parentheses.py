class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        count = 0
        for i in s:
            if i == "(":
                stack.append(count)
                count = 0
            else:
                last = stack.pop()
                count = last + max(2 * count, 1)
        return count

        