# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None and root2 is None:
            return None
        if root1 is not None and root2 is None:
            return root1
        if root1 is None and root2 is not None:
            return root2
        # Root of the merged tree.
        root = TreeNode(root1.val + root2.val)
        # Merge the left and right subtrees.
        root.left = self.mergeTrees(root1.left, root2.left)
        root.right = self.mergeTrees(root1.right, root2.right)
        return root
