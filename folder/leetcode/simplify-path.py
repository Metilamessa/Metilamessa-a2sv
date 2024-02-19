class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split('/')
        for i in path:
            if i and i != ".":
                if i == "..":
                    if stack:
                        stack.pop()
                else:
                    stack.append(i)
        stack = "/".join(stack)
        return "/" + stack
