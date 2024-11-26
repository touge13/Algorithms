class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
# O(n * m)
        if len(strs) == 0: 
            return ""
        s1, s2 = min(strs), max(strs)
        i = 0
        while i < len(s1) and i < len(s2) and s1[i] == s2[i]: 
            i += 1
        return s1[:i]

# O(n * m)
#        w = strs[0]
#        l = len(strs[0])
#        for i in range(1, len(strs)):
#            l = min(l, len(strs[i]))
#            for j in range(min(len(w), len(strs[i]))):
#                if w[j] != strs[i][j]:
#                    l = min(l, j)
#        return w[:l]
