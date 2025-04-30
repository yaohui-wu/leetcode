from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Breadth-first search.
        if root is None:
            return []
        answer = []
        queue = deque([root])
        while len(queue) != 0:
            level = [] # Store values at the current level.
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                # Add children nodes for the next level.
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            answer.append(level)
        return answer
