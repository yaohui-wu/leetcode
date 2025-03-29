# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        size = len(nums) # Size of the BST.
        # Empty BST.
        if size == 0:
            return None
        # BST with one node.
        if size == 1:
            return TreeNode(nums[0])
        mid = size // 2 # Index of the middle element of the array.
        root = TreeNode(nums[mid]) # Root of the BST.
        # Recursively build the left and right subtrees.
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root
