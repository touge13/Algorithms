class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i in s:
            d[i] = 1 + d.get(i, 0)
        for i in range(len(s)):
            if d[s[i]] == 1:
                return i
        return -1
