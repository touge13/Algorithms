class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        leftSum = 0
        for i in range(len(nums)):
            totalSum -= nums[i]
            if leftSum == totalSum:
                return i
            leftSum += nums[i]
        return -1
