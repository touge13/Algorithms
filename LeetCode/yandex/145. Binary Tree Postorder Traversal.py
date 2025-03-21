# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def helper(root, res):
            if root is not None:
                helper(root.left, res)
                helper(root.right, res)
                res.append(root.val)
        res = []
        helper(root, res)
        return res
