class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        l = r = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                res = max(res, r - l)
                l = r + 1
        res = max(res, r + 1 - l)
        return res 
