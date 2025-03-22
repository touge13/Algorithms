# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(N) но все равно beats 20%
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def helper(root):
            if root is None:
                return 0
            else:
                cur = 0
                if low <= root.val <= high:
                    cur += root.val
                cur += helper(root.left)
                cur += helper(root.right)
                return cur
        res = helper(root)
        return res   
