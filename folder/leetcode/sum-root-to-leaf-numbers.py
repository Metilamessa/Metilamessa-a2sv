# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def path(curr, psum):
            if not curr:
                return 0
            psum = (psum * 10) + curr.val
            if not curr.left and not curr.right:
                return psum
            return path(curr.left, psum) + path(curr.right,psum)
        return path(root, 0)