class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for s in strs:
            hashMap.setdefault(''.join(sorted(s)), []).append(s)
        return list(hashMap.values())