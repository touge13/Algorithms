class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        res = 0
        uniq = {}
        for n in nums:
            uniq[n] = 1 + uniq.get(n, 0)
        for u in uniq:
            if k == 0:
                if uniq[u] > 1:
                    res += 1
            else:
                if u + k in uniq:
                    res += 1
        return res
