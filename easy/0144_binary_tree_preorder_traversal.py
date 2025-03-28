# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Empty tree.
        if root is None:
            return []
        # Preorder traversal: root -> left -> right.
        preorder = [root.val]
        preorder += self.preorderTraversal(root.left)
        preorder += self.preorderTraversal(root.right)
        return preorder
