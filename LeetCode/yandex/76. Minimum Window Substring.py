# O(N)
class Solution:    
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        ds = {}
        dt = {}
        for i in t:
            dt[i] = 1 + dt.get(i, 0)
            
        minLen = float("inf")
        res = ""
        l = 0
        for r in range(len(s)):
            ds[s[r]] = 1 + ds.get(s[r], 0)    
            while all(ds.get(char, 0) >= dt.get(char, 0) for char in dt):
                if sum(ds.values()) <= minLen:
                    minLen = sum(ds.values())
                    if minLen >= ((r + 1) - l):
                        res = s[l:r+1]
                        
                if ds[s[l]] == 1:
                    del ds[s[l]]
                else:
                    ds[s[l]] -= 1
                    
                l += 1
        return res
