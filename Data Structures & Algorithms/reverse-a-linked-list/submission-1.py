# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        revList =  None

        node = head

        while node:
            nodeNext = node.next

            node.next = revList
            revList = node

            node = nodeNext

        return revList