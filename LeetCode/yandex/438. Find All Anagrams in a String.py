class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = [] 

        charsOfP = {}
        for char in p:
            if char in charsOfP:
                charsOfP[char] += 1
            else:
                charsOfP[char] = 1

        chars = {} 
        l = r = 0
        while r < len(s):
            if r - l + 1 <= len(p):
                if s[r] in chars:
                    chars[s[r]] += 1
                else:
                    chars[s[r]] = 1
                r += 1
            else:
                if chars[s[l]] == 1:
                    del chars[s[l]]
                else:
                    chars[s[l]] -= 1
                l += 1

            if chars == charsOfP:
                res.append(l)
                
        return res
