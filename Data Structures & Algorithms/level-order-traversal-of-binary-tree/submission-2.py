# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #base case
        if not root:
            return []

        leftOrder = self.levelOrder(root.left)
        rightOrder = self.levelOrder(root.right)
        comb = [[root.val]]

        #run the combination algo for len of smaller list
        print("____")
        print(leftOrder)
        print(rightOrder)
        print(min(len(leftOrder),len(rightOrder)))

        for i in range(min(len(leftOrder),len(rightOrder))):
            print(i)
            comb.append(leftOrder[i] + rightOrder[i])

        #then add remaining items from larger list

        if len(leftOrder) < len(rightOrder):
            for i in range(len(leftOrder),len(rightOrder)):
                comb.append(rightOrder[i])
        else:
            for i in range(len(rightOrder), len(leftOrder)):
                comb.append(leftOrder[i])
     
                


        return comb