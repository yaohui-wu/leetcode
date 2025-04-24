from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # Initialize frontiers for bidirectional BFS.
        start_set = set(["0000"])
        target_set = set([target])
        # Track visited combinations to avoid revisiting and deadends.
        visited = set(deadends)
        # Early exit if start or target is a deadend.
        if "0000" in visited or target in visited:
            return -1
        moves = 0
        while len(start_set) != 0 and len(target_set) != 0:
            # Always expand the smaller frontier for efficiency.
            if len(start_set) > len(target_set):
                start_set, target_set = target_set, start_set
            next_level = set() # Next level of combinations.
            for s in start_set:
                if s in target_set:
                    return moves
                if s not in visited:
                    visited.add(s)
                    # Add all valid neighbors to the next level.
                    for neighbor in self.neighbors(s):
                        if neighbor not in visited:
                            next_level.add(neighbor)
            # Move to the next level.
            start_set = next_level
            moves += 1
        # No solution found.
        return -1
    
    def neighbors(self, s):
        neighbors = []
        for i in range(4):
            neighbors.append(s[:i] + str((int(s[i]) + 1) % 10) + s[i + 1:])
            neighbors.append(s[:i] + str((int(s[i]) - 1) % 10) + s[i + 1:])
        return neighbors
