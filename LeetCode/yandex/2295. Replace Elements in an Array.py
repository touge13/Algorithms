class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        d = {} 
        for i in range(len(nums)):
            d[nums[i]] = i
        for o in operations:
            nums[d[o[0]]] = o[1]
            d[o[1]] = d[o[0]]
        return nums
