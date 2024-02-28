# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        prev_root = None
        max_mod = 0
        curr_mod = 0
        
        def dfs(root):
            nonlocal  prev_root, max_mod, curr_mod, res
            if root == None:
                return 
            
            dfs(root.left)
            if root.val == prev_root:
                curr_mod += 1
            else:
                curr_mod = 1
            if curr_mod > max_mod:
                max_mod = curr_mod
                res= [root.val]
            elif curr_mod == max_mod:

                res.append(root.val)
            prev_root = root.val
            dfs(root.right)
        
        dfs(root)
        return res
        

       