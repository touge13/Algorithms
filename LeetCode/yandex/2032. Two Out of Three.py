class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        d = {}
        s1 = set(nums1)
        for n in s1:
            d[n] = 1 + d.get(n, 0)
        s2 = set(nums2)
        for n in s2:
            d[n] = 1 + d.get(n, 0)
        s3 = set(nums3)
        for n in s3:
            d[n] = 1 + d.get(n, 0)
        res = []
        for n in d:
            if d[n] >= 2:
                res.append(n)
        return res
