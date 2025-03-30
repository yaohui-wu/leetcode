from collections import deque

class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)
        size = len(self.queue)
        # Rotate the queue to maintain the stack order.
        for _ in range(size - 1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        if self.empty():
            return None
        return self.queue.popleft()

    def top(self) -> int:
        if self.empty():
            return None
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
