class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = {}
        for ch in magazine:
            d[ch] = 1 + d.get(ch, 0)
        for ch in ransomNote:
            if ch in d:
                d[ch] -= 1
                if d[ch] == 0:
                    del d[ch]
            else:
                return False
        return True
