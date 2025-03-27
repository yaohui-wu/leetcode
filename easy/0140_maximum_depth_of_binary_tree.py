# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        # Maximum depth of left subtree.
        max_left = self.maxDepth(root.left)
        # Maximum depth of right subtree.
        max_right = self.maxDepth(root.right)
        # Maximum depth of the tree is the maximum depth of the left and right
        # subtree plus 1 for the root.
        max_depth = max(max_left, max_right) + 1
        return max_depth
