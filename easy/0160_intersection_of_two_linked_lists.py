# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None or headB is None:
            return None
        a = headA
        b = headB
        while a != b:
            # If a or b reaches the end of the list, reset it to the head of
            # the other list.
            if a is None:
                a = headB
            else:
                a = a.next
            if b is None:
                b = headA
            else:
                b = b.next
        # a and b are either the same node or both are None.
        return a
