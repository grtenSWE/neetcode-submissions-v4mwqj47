# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#better implementation to avoid list concatenation 
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        
        def dfs(root): #returns the order list
            if root is None:
                return
       
            dfs(root.left) 

            if len(arr) == k:
                return 

            arr.append(root.val)

            if len(arr) == k:
                return 

            dfs(root.right)

        dfs(root)
        return arr[-1]