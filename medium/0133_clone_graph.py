"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            # Empty graph.
            return None
        # Map original node value to its clone.
        clones = {node.val: Node(node.val)}
        queue = deque([node])
        while len(queue) != 0:
            curr = queue.popleft()
            clone = clones[curr.val]
            for neighbor in curr.neighbors:
                if neighbor.val not in clones:
                    # Clone unvisited neighbor.
                    clones[neighbor.val] = Node(neighbor.val)
                    queue.append(neighbor)
                # Link the clone to the neighbor clone.
                clone.neighbors.append(clones[neighbor.val])
        # Return the clone of the original entry node.
        return clones[node.val]
