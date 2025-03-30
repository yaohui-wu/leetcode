from collections import deque

class MyQueue:

    def __init__(self):
        self.stack1 = deque() # Main stack for enqueue.
        self.stack2 = deque() # Auxiliary stack for dequeue.

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if self.peek() is None:
            return None
        return self.stack2.pop()

    def peek(self) -> int:
        # Transfer elements from stack1 to stack2 if stack2 is empty.
        if len(self.stack2) == 0:
            size = len(self.stack1)
            # Queue is empty.
            if size == 0:
                return None
            # Reverse order in stack2.
            for _ in range(size):
                self.stack2.append(self.stack1.pop())
        # Top of stack2 is the front of the queue.
        return self.stack2[-1]

    def empty(self) -> bool:
        return len(self.stack1) == 0 and len(self.stack2) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
