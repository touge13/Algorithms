class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        d = {}
        res = -1
        for n in nums:
            if -n in d:
                res = max(abs(res), abs(n))
            else:
                d[n] = 1 + d.get(n, 0)
        return res
