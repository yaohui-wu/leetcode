# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(None) # Dummy node.
        curr = head
        carry = False # Carry over from the previous addition.
        # Continue until both lists are fully traversed and no carry remains.
        while l1 is not None or l2 is not None or carry:
            sum = 0 # Sum of the current digits plus any carry.
            if l1 is not None:
                sum += l1.val
                l1 = l1.next
            if l2 is not None:
                sum += l2.val
                l2 = l2.next
            if carry:
                sum += 1
                carry = False
             # Check if the sum results in a carry for the next digit.
            if sum >= 10:
                carry = True
                sum %= 10 # Keep only the single-digit part.
            curr.next = ListNode(sum)
            curr = curr.next
        head = head.next
        return head
