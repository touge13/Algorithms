class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        l1 = []
        for ch in s:
            if ch == "#" and len(l1) != 0:
                l1.pop()
            elif ch != "#":
                l1.append(ch)
        l2 = []
        for ch in t:
            if ch == "#" and len(l2) != 0:
                l2.pop()
            elif ch != "#":
                l2.append(ch)
        return l1 == l2 
