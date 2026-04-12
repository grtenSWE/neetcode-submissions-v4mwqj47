# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
 

        if not p and not q: #if both are None
            return True
      
        #if only one is none then also return False
        if p and not q or not p and q:
            return False
            
        if p.val != q.val: #if the values of both aren't the same
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


