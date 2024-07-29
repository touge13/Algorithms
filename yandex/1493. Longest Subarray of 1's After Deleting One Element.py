class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        lSide = rSide = res = 0
        allOnes = 1
        for i in range(len(nums)):
            if nums[i] == 1:
                rSide += 1
            else:
                res = max(res, rSide + lSide)
                lSide = rSide
                rSide = 0
                allOnes = 0
        res = max(res, rSide + lSide)    
        if allOnes == 1:
            return res - 1
        else:
            return res
