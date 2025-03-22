class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1, 2, 3, 4]
        # output:
        # для каждого элемента посчитаем произведение всех элементов слева (не включая его самого) (если элемент первый, то произведение слева =1) [1, 1, 2, 6]
        # для каждого элемента посчитаем произведение всех элементов справа (не включая его самого) (если элемент последний, то произведение справа =1) [24, 12, 4, 1]
        # результат - поэлементное умножение
        output = [1] * len(nums)
        left = 1
        for i in range(len(nums)):
            output[i] *= left
            left *= nums[i]
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= right
            right *= nums[i]
        return output
