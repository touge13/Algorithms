class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sht = {}
        tht = {}
        
        for i in s:
            if i in sht:
                sht[i] += 1
            else:
                sht[i] = 1

        for i in t:
            if i in tht:
                tht[i] += 1
            else:
                tht[i] = 1
        
        if sht == tht:
            return True
        else:
            return False
