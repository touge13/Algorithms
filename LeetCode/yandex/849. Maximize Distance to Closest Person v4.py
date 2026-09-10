class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        l = r = 0
        res = 0
        for r in range(len(seats)):
            if seats[r] == 1:
                if l == 0 and seats[l] == 0:
                    res = max(res, r)
                else:
                    res = max(res, (r - l) // 2)
                l = r
        res = max(res, r - l)
        return res
