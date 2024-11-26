# O(N)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # S_n = (a_1 + a_n) * n/2 
        # a_1 = 0; a_n = len(nums); n = len(nums) + 1
        difference = len(nums) * (len(nums) + 1) / 2 - sum(nums)
        if difference == 0:
            if 0 in nums:
                return len(nums)
            else:
                return 0
        else:
            return int(difference)
