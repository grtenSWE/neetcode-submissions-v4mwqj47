# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #traverse to end of list, and record the length
        nodeL = head
        node = head

        length = 0

        while node:
            node = node.next
            length += 1

        node = head

        for i in range(length//2):
            for _ in range((length - 1) - 2*i):
                node = node.next
                print(node.val)

            nodeLtmp = nodeL.next
            nodeL.next = node
            node.next = nodeLtmp
            nodeL = nodeLtmp
            node = nodeL

        nodeL.next = None

        print("___")

     