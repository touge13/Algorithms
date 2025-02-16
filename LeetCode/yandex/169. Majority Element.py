class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        t = len(nums) / 2
        for n in nums:
            d[n] = 1 + d.get(n, 0)
            if d[n] > t:
                return n
