# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        middle = head
        while head is not None and head.next is not None:
            middle = middle.next # Move one step.
            head = head.next.next # Move two steps.
        # If length of linked list is odd, middle will be the exact middle.
        # If length of linked list is even, middle will be the second middle.
        return middle
