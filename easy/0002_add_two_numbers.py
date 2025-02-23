# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(None)
        curr = head
        carry = False
        while l1 is not None or l2 is not None:
            sum = 0
            if l1 is not None:
                sum += l1.val
                l1 = l1.next
            if l2 is not None:
                sum += l2.val
                l2 = l2.next
            if carry:
                sum += 1
                carry = False
            if sum >= 10:
                carry = True
                sum %= 10
            curr.next = ListNode(sum)
            curr = curr.next
        if carry:
            curr.next = ListNode(1)
        head = head.next
        return head
