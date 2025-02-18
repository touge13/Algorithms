class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        d1 = {}
        for s in s1:
            d1[s] = 1 + d1.get(s, 0)
        d2 = {}
        for i in range(len(s1)):
            d2[s2[i]] = 1 + d2.get(s2[i], 0)
        if d1 == d2:
            return True
        l = 0
        for r in range(len(s1), len(s2)):
            d2[s2[r]] = 1 + d2.get(s2[r], 0)
            d2[s2[l]] -= 1
            if d2[s2[l]] == 0:
                del d2[s2[l]]
            l += 1
            if d1 == d2:
                return True
        return False
