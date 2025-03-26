# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        curr = head
        result = curr
        while head is not None and head.next is not None:
            if head.val != head.next.val:
                curr.next = head.next
                curr = curr.next
            head = head.next
        curr.next = None
        return result
