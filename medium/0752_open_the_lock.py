from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = deque(["0000"])
        visited = set(deadends)
        if "0000" in visited:
            return -1
        steps = 0
        while len(queue) != 0:
            for _ in range(len(queue)):
                s = queue.popleft()
                if s == target:
                    return steps
                for neighbor in self.neighbors(s):
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
            steps += 1
        return -1
    
    def neighbors(self, s):
        neighbors = []
        for i in range(4):
            neighbors.append(s[:i] + str((int(s[i]) + 1) % 10) + s[i + 1:])
            neighbors.append(s[:i] + str((int(s[i]) - 1) % 10) + s[i + 1:])
        return neighbors
