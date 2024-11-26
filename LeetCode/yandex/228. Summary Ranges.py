class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        start = final = 0
        res = []
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [str(nums[0])]
            
        for i in range(len(nums)):
            if i != 0:
                if nums[i] == nums[i - 1] + 1 :
                    final = i
                else:
                    if nums[start] == nums[final]:
                        res.append(str(nums[start]))
                    else:
                        res.append(str(nums[start]) + "->" + str(nums[final]))
                    start = final = i
        if nums[start] == nums[final]:
            res.append(str(nums[start]))
        else:
            res.append(str(nums[start]) + "->" + str(nums[final]))
        return res