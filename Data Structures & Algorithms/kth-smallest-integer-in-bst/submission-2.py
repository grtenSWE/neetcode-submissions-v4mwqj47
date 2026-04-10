# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#solved in 35 mins

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def dfs(root): #returns the order list
            if root is None:
                return []
       
            return dfs(root.left) + [root.val] + dfs(root.right)


        return dfs(root)[k-1]


