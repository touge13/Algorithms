class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        d1 = {}
        for ch in p:
            d1[ch] = 1 + d1.get(ch, 0)
        d2 = {}
        l = 0
        for r in range(len(s)):
            d2[s[r]] = 1 + d2.get(s[r], 0)
            if r - l + 1 > len(p):
                d2[s[l]] -= 1
                if d2[s[l]] == 0: del d2[s[l]]
                l += 1
            if d1 == d2:
                res.append(l)
        return res
