class Solution:
    def maxPower(self, s: str) -> int:
        res = 0
        l = 0 
        for r in range(len(s)):
            if s[r] == s[l]:
                res = max(res, r - l + 1)
            else:
                l = r
        return res 
