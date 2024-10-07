class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        mid = (len(nums) - 1) // 2
        res = len(nums)
        i = 0
        j = mid + 1
        while i <= mid and j < len(nums):
            if nums[i] < nums[j]:
                res -= 2
            i += 1
            j += 1
        return res

