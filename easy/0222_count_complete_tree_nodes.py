# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left_depth = self.depth(root.left)
        right_depth = self.depth(root.right)
        # Left subtree is a perfect binary tree.
        # Right subtree is a complete binary tree.
        if left_depth == right_depth:
            count = 2 ** left_depth
            return count + self.countNodes(root.right)
        # Left subtree is a complete binary tree.
        # Right subtree is a perfect binary tree.
        count = 2 ** right_depth
        return count + self.countNodes(root.left)
    
    def depth(self, root):
        if root is None:
            return 0
        # The binary tree is complete.
        return 1 + self.depth(root.left)
