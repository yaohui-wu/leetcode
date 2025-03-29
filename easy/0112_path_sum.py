# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Empty tree has no root-to-leaf paths.
        if root is None:
            return False
        if root.left is None and root.right is None:
            return root.val == targetSum
        sum = targetSum - root.val
        return (self.hasPathSum(root.left, sum)
                or self.hasPathSum(root.right, sum))
