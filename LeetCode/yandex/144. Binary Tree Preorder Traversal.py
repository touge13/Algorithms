# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def helper(root, res):
            if root is not None:
                res.append(root.val)
                helper(root.left, res)
                helper(root.right, res)
        res = []
        helper(root, res)
        return res 
