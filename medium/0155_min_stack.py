class MinStack:

    def __init__(self):
        # Linked list to store values and minimums.
        self.head = None # Top of the stack has the minimum value.

    def push(self, val: int) -> None:
        # Update head of linked list with given value and new minimum.
        if self.head is None:
            self.head = self.Node(val, val, None)
        else:
            self.head = self.Node(val, min(val, self.head.min), self.head)

    def pop(self) -> None:
        # Remove top by updating head to next node.
        self.head = self.head.next

    def top(self) -> int:
        return self.head.value

    def getMin(self) -> int:
        return self.head.min
    
    class Node:

        def __init__(self, value, min, next):
            self.value = value
            self.min = min
            self.next = next

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
