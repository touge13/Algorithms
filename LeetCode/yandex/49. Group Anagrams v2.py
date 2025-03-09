class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {''.join(sorted(s)) : [] for s in strs}
        for s in strs:
            d[''.join(sorted(s))].append(s)
        return list(d.values())
