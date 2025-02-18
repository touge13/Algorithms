class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        p2 = 0
        for p1 in range(len(s)):
            if p2 == len(t):
                return 0
            if s[p1] == t[p2]:
                p1 += 1
                p2 += 1
        return len(t) - p2
