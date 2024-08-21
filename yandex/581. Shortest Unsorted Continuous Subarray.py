class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < len(nums) - 1 and nums[l + 1] >= nums[l]:
            l += 1
        while r > 1 and nums[r - 1] <= nums[r] and l < r:
            r -= 1

        temp = nums[l:r+1]
        tempMin = min(temp)
        tempMax = max(temp)
        while l > 0 and tempMin < nums[l-1]:
            l -= 1
        while r < len(nums) - 1 and tempMax > nums[r+1]:
            r += 1

        if l == r:
            return 0
        else:
            return r - l + 1
