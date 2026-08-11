# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        depth = 0
        tail = head
        while tail is not None:
            tail = tail.next
            depth +=1
        # print(f"Depth: {depth} - {depth // 2}")

        current = 1
        while current <= depth // 2:
            head = head.next
            current += 1

        return head
        