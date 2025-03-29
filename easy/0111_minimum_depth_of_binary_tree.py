# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # Empty tree.
        if root is None:
            return 0
        min_depth = 0
        # # Minimum depth of left subtree.
        left_depth = self.minDepth(root.left)
        # Minimum depth of right subtree.
        right_depth = self.minDepth(root.right)
        # Minimum depth of the tree is the minimum depth of the left and right
        # subtree plus 1 for the root.
        if left_depth == 0 or right_depth == 0:
            min_depth = left_depth + right_depth + 1
        else:
            min_depth = min(left_depth, right_depth) + 1
        return min_depth
