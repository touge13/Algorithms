class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d1 = {}
        d2 = {}
        sList = s.split(" ")
        if len(sList) != len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] in d1:
                if d1[pattern[i]] != sList[i]:
                    return False
            else:
                d1[pattern[i]] = sList[i]
            
            if sList[i] in d2:
                if d2[sList[i]] != pattern[i]:
                    return False
            else:
                d2[sList[i]] = pattern[i]
        return True
