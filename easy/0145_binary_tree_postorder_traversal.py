# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Empty tree.
        if root is None:
            return []
        # Postorder traversal: left -> right -> root.
        postorder = self.postorderTraversal(root.left)
        postorder += self.postorderTraversal(root.right)
        postorder.append(root.val)
        return postorder
