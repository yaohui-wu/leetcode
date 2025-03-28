# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Empty tree.
        if root is None:
            return root
        left = root.left # Save the left subtree.
        root.left = self.invertTree(root.right) # Invert the right subtree.
        root.right = self.invertTree(left) # Invert the left subtree.
        return root
