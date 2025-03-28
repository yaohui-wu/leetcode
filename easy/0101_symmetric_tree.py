# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Empty tree is trivially symmetric.
        # Check if the the left and right subtrees are mirrors of each other.
        return root is None or self.isMirror(root.left, root.right)
    
    def isMirror(self, left, right):
        # If either of the subtrees is None, they are symmetric only if both
        # are None.
        if left is None or right is None:
            return left == right
        # Check if the current nodes are equal and their subtrees are mirrors.
        return (left.val == right.val
                and self.isMirror(left.left, right.right)
                and self.isMirror(left.right, right.left))
