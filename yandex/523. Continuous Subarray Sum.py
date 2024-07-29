class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainders = {0:-1}
        prefixSum = 0
        for i in range(len(nums)):
            prefixSum += nums[i]
            if (prefixSum) % k in remainders:
                if i - remainders[(prefixSum) % k] >= 2:
                    return True
            else:
                remainders[(prefixSum) % k] = i     
        return False


            
        