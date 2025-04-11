# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Start the validation without bounds.
        return self.is_valid_bst(root, None, None)
    
    def is_valid_bst(self, root, min_node, max_node):
        if root is None:
            return True
        # Check if the current node's value is within the bounds.
        if min_node is not None and root.val <= min_node.val:
            return False
        if max_node is not None and root.val >= max_node.val:
            return False
        # Recursively check the left and right subtrees with updated bounds.
        return (self.is_valid_bst(root.left, min_node, root)
                and self.is_valid_bst(root.right, root, max_node))
