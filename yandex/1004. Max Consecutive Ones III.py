class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = 0
        numZeros = 0
        l = r = 0
        while r < len(nums):
            if nums[r] == 0:
                numZeros += 1
                
            if numZeros > k:
                if nums[l] == 0:
                    numZeros -= 1
                l += 1
            
            if numZeros <= k:
                res = max(res, r - l + 1)

            r += 1 
        return res
