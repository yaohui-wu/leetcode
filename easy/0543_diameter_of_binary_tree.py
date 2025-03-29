# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_depth(root)
        return self.diameter
    
    def max_depth(self, root):
        # Empty tree.
        if root is None:
            return 0
        left_depth = self.max_depth(root.left) # Depth of left subtree.
        right_depth = self.max_depth(root.right) # Depth of right subtree.
        # Update the diameter if the path through the root is longer.
        self.diameter = max(self.diameter, left_depth + right_depth)
        # Return the maximum depth of the tree.
        return max(left_depth, right_depth) + 1
