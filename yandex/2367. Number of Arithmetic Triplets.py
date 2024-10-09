class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        d = {}
        res = 0
        for n in nums:
            if (n - diff in d) and (n - 2 * diff in d):
                res += 1
            d[n] = 1 + d.get(n, 0)
        return res
