# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.height(root) != -1
    
    def height(self, root):
        if root is None:
            return 0
        # Height of left subtree.
        left_height = self.height(root.left)
        if left_height == -1:
            return -1
        # Height of right subtree.
        right_height = self.height(root.right)
        if right_height == -1:
            return -1
        # Check if the current tree is height-balanced.
        if abs(left_height - right_height) > 1:
            return -1
        # Return the height of the current tree.
        return max(left_height, right_height) + 1
