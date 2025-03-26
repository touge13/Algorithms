# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, low, high):
            if root is None:
                return True
            else:
                if low < root.val < high:
                    return helper(root.left, low, root.val) and helper(root.right, root.val, high)
                else:
                    return False
        high = float("inf")
        low = float("-inf")
        return helper(root, low, high)
