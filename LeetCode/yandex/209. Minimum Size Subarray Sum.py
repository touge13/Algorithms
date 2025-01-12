class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        res = float("inf")
        s = 0
        for r in range(len(nums)):
            s += nums[r]
            while s >= target:
                res = min(res, r - l + 1)
                s -= nums[l]
                l += 1
        if res == float("inf"): 
            return 0 
        else: 
            return res
