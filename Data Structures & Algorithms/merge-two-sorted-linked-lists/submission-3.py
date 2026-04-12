# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #we insert list1 into list2

        head = ListNode(-101,list2)
        list2Last = head

        while list1 is not None:
            if not list2:
                list2Last.next = list1
                break
           
            if list1.val < list2.val:
                list1Tmp = list1.next
                list1.next = list2
                list2Last.next = list1
                list2Last = list1
                list1 = list1Tmp
            else:
                list2Last = list2
                list2 = list2.next

        return head.next

            


            

