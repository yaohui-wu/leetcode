# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        size = 0
        middle = head
        while head is not None:
            size += 1
            head = head.next
        for _ in range(size // 2):
            middle = middle.next
        return middle
