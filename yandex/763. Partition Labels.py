class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {s[i]: i for i in range(len(s))}
        res = []
        r = 0
        while r < len(s):
            final = last[s[r]]
            j = r
            while j < final:
                if last[s[j]] > final:
                    final = last[s[j]]
                j += 1
            res.append(final - r + 1)
            r = final + 1
        return res
