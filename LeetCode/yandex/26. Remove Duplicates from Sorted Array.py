class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        res = 1
        for r in range(len(nums)):
            if nums[l] != nums[r]:
                nums[l + 1] = nums[r]
                res += 1
                l += 1
        return res
