# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        self.InTrav(root , res)
        return res[k-1]
 

    def InTrav(self , root, res ):
        if root == None:
            return None
        self.InTrav(root.left , res)
        res.append(root.val)       
        self.InTrav(root.right , res)   
      
        