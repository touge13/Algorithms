class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j = set(jewels)
        res = 0
        for s in stones:
            if s in j:
                res += 1
        return res
