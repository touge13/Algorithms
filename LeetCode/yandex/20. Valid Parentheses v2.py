class Solution:
    def isValid(self, s: str) -> bool:
        d1 = {'(':')', '[':']', '{':'}'}
        d2 = []
        for p in s:
            if p in d1:
                d2.append(p)
            elif d2 and d2[-1] in d1 and p == d1[d2[-1]]:
                d2.pop()
            else:
                d2.append(p)
        return not d2
