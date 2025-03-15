class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        d = {}
        for n in nums1:
            d[n] = 1 + d.get(n, 0)
        for n in nums2:
            if n in d:
                res.append(n)
                d[n] -= 1
                if d[n] == 0: del d[n]
        return res
