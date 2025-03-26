# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def helper(root):
            if not root:
                return None
            # идем влево
            res = helper(root.left)
            if res:
                return res
            # проверяем k
            # nonlocal позволяет изменять k, 
            # потому что она находится в ближайшей внешней функции
            nonlocal k 
            k -= 1
            if k == 0:
                return root
            # идем вправо
            return helper(root.right)
        root = helper(root)
        return root.val
