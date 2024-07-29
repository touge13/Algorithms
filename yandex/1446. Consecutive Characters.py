class Solution:
    def maxPower(self, s: str) -> int:
        l = r = 0
        res = 0
        while r < len(s):
            if s[r] == s[l]:
                r += 1
            else:
                l = r
                r += 1
            res = max(res, r - l)
        return res