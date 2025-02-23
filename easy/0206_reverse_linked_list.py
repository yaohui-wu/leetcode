# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Head of the reversed linked list.
        curr = None
        # Iterate through the original linked list.
        while head is not None:
            next = curr
            # The current node of the original linked list is the new head of
            # the reversed linked list.
            curr = head
            # Move the head of the original linked list.
            head = head.next
            # Attach the rest of the reversed linked list.
            curr.next = next
        return curr
