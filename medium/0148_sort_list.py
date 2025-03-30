# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        # Get the size of the linked list.
        size = self.size(head)
        list = ListNode() # Dummy head of the sorted linked list.
        list.next = head
        # Bottom-up merge sort.
        step = 1
        while step < size:
            curr = list.next
            tail = list
            while curr is not None:
                left = curr
                right = self.split(left, step)
                curr = self.split(right, step)
                tail = self.merge(left, right, tail)
            step *= 2
        return list.next
    
    def size(self, head):
        size = 0
        curr = head
        while curr is not None:
            size += 1
            curr = curr.next
        return size
    
    def split(self, head, n):
        # Split the linked list into two halves.
        # The first half of the linked list has at most n nodes.
        for _ in range(1, n):
            if head is None:
                return None
            head = head.next
        if head is None or head.next is None:
            return None
        second = head.next
        head.next = None
        # Return the second half of the linked list.
        return second
        
    
    def merge(self, list1, list2, head):
        # Merge two sorted linked lists and append the result to head.
        curr = head
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        if list1 is not None:
            curr.next = list1
        elif list2 is not None:
            curr.next = list2
        while curr.next is not None:
            curr = curr.next
        # Return the tail of the merged linked list.
        return curr
