class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        d1 = {}
        for w in words1:
            d1[w] = 1 + d1.get(w, 0)
        d2 = {}
        for w in words2:
            d2[w] = 1 + d2.get(w, 0)
        res = 0
        for w in d1:
            if w in d1 and w in d2:
                if d1[w] == 1 and d2[w] == 1:
                    res += 1
        return res 
