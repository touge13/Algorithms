class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        res = 0
        d = {}
        for n in nums:
            if k - n in d:
                res += 1
                if d[k - n] == 1:
                    del d[k-n]
                else:
                    d[k - n] -= 1
            else:
                d[n] = 1 + d.get(n, 0)
        return res
