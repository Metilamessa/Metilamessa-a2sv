# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def pre(root, curMin, curMax):
            nonlocal ans 
            if not root:
                ans = max(ans, curMax - curMin)
                return
            curMin = min(curMin, root.val)
            curMax = max(curMax, root.val)

            pre(root.left, curMin, curMax)
            pre(root.right, curMin, curMax)
        ans = 0

        pre(root,root.val,root.val)
        return  ans
