class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d = {}
        for ch in s:
            d[ch] = 1 + d.get(ch, 0)
        t = d[s[0]]
        for i in d.values():
            if i != t:
                return False
        return True
