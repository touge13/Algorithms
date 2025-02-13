class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
      
        temp = 0
        for i in range(len(nums)):
            res[i] = temp
            temp += nums[i]
          
        temp = 0
        for i in range(len(nums) - 1, -1, -1):
            res[i] = abs(res[i] - temp)
            temp += nums[i]
          
        return res
