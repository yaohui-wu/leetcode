# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Check if either tree is None.
        if p is None or q is None:
            # Two trees are the same if both are None.
            return p == q
        # Check if the values of both roots are the same.
        if p.val != q.val:
            return False
        # Check if the left and right subtrees are the same.
        return (self.isSameTree(p.left, q.left)
                and self.isSameTree(p.right, q.right))
