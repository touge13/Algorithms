class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        l = 0
        if len(nums) == 0: return []
        if len(nums) == 1: return [str(nums[0])]
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1] + 1:
                if nums[l] == nums[r - 1]:
                    res.append(f"{nums[l]}")
                else:
                    res.append(f"{nums[l]}->{nums[r - 1]}")
                l = r
        if nums[l] == nums[r]:
            res.append(f"{nums[l]}")
        else:
            res.append(f"{nums[l]}->{nums[r]}")
        return res 
