# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Base case: empty tree.
        if root is None:
            return []
        inorder = []
        # Traverse the left subtree, the root, then the right subtree.
        inorder += self.inorderTraversal(root.left)
        inorder.append(root.val)
        inorder += self.inorderTraversal(root.right)
        return inorder
