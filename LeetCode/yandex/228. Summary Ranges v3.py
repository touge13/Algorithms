class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        res = []
        l = r = 0
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1] + 1:
                if nums[l] == nums[r - 1]:
                    res.append(str(nums[l]))
                else:
                    res.append(f"{nums[l]}->{nums[r - 1]}")
                l = r
        if nums[l] == nums[r]:
            res.append(str(nums[l]))
        else:
            res.append(f"{nums[l]}->{nums[r]}")
        return res
