class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = 0
        decreasing = 0
        for r in range(1, len(nums)):
            if nums[r] > nums[r - 1]:
                increasing = 1
            elif nums[r] < nums[r - 1]:
                decreasing = 1
        if increasing and decreasing: 
            return False
        else:
            return True
