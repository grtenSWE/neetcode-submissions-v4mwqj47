# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        return self.check(root)

    def check(self, node, lower=-1001, upper=1001):
        if node == None:
            return True

        if lower < node.val < upper:
            return self.check(node.left, lower, node.val) and self.check(node.right, node.val, upper)
        
        return False



      











        