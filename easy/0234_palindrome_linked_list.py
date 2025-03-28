# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Find the middle of the linked list.
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        # Reverse the second half of the linked list.
        prev = slow
        slow = slow.next
        prev.next = None
        while slow is not None:
            next = prev
            prev = slow
            slow = slow.next
            prev.next = next
        # Compare the first half and the reversed second half.
        curr = prev
        while curr is not None:
            if curr.val != head.val:
                return False
            curr = curr.next
            head = head.next
        return True
