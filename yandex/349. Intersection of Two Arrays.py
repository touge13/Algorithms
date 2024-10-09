class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = set()
        for n in nums1:
            n1.add(n)
        n2 = set()
        for n in nums2:
            n2.add(n)
        res = []
        for n in n2:
            if n in n1:
                res.append(n)
        return res
