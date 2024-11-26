class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hm = {}
        for i in nums1:
            hm[i] = 1 + hm.get(i, 0) 
        res = []
        for i in nums2:
            if i in hm:
                if hm[i] == 1:
                    del hm[i]
                else:
                    hm[i] -= 1
                res.append(i)
        return res
