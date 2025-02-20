# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = None
        prev = head
        while prev is not None:
            next = curr
            curr = prev
            prev = prev.next
            curr.next = next
        return curr
