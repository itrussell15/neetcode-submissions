# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode()
        tail = head

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                next_ = list1.val
                list1 = list1.next
            else:
                next_ = list2.val
                list2 = list2.next
            tail.next = ListNode(val=next_)
            tail = tail.next
        
        if list1 is not None:
            tail.next = list1
        else:
            tail.next = list2

        return head.next

        