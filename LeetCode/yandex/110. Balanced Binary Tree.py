# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            if not root:
                return 0
            left_height = helper(root.left)
            if left_height == -1:
                return -1
            right_height = helper(root.right)
            if right_height == -1:
                return -1
            if abs(left_height - right_height) > 1:
                return -1 
            return max(left_height, right_height) + 1
        return helper(root) != -1 

# Пример   
#         1
#        / \
#       2   3
#      / \
#     4   5
# Начинаем с корня 1.
#     Рекурсивно вызываем helper для левого поддерева (2):
#       Вызываем helper для левого поддерева 4:
#           4 — лист, возвращаем 0.
#       Вызываем helper для правого поддерева 5:
#           5 — лист, возвращаем 0.
#       Высота узла 2 равна max(0, 0) + 1 = 1.
#     Рекурсивно вызываем helper для правого поддерева (3):
#           3 — лист, возвращаем 0.
#       Проверяем баланс корня 1:
#           Левая высота = 1, правая высота = 0.
#       Разница = abs(1 - 0) = 1, что <= 1.
#       Высота корня 1 равна max(1, 0) + 1 = 2.
# Результат: дерево сбалансировано.
            
