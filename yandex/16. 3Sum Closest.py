# O(N^2)
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == target:
                    return s
                if abs(target - s) < abs(target - res):
                    res = s
                if s > target:
                    k -= 1
                elif s < target:
                    j += 1
        return res
