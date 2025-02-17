class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        d1 = {}
        for w in word1:
            d1[w] = 1 + d1.get(w, 0)
        d2 = {}
        for w in word2:
            d2[w] = 1 + d2.get(w, 0)
        for w in d1:
            if w in d2 and abs(d1[w] - d2[w]) > 3:
                return False
            elif w not in d2 and d1[w] > 3:
                return False
        for w in d2:
            if w in d1 and abs(d1[w] - d2[w]) > 3:
                return False
            elif w not in d1 and d2[w] > 3:
                return False
        return True
