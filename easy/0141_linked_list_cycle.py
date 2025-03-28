# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        while fast is not None and fast.next is not None:
            head = head.next # Move one step.
            fast = fast.next.next # Move two steps.
            # If there is a cycle, the two pointers will meet.
            if head == fast:
                return True
        return False
