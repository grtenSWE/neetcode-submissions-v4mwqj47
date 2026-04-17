# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #the intersection of 2 sets
        
        pList = {}
        qList = {}

        def dfs(node, x, setx):
            if node.val == x.val:
                setx[node] = None
                return

            setx[node] = None

            if x.val < node.val:
                dfs(node.left, x, setx)
            else:
                dfs(node.right, x, setx)

        dfs(root, p, pList)
        dfs(root, q, qList)

        for node in reversed(pList):
            if node in qList:
                return node

  
            