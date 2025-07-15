class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        l = 0
        res = 0
        for r in range(len(seats)):
            if seats[r] == 1:
                if l == 0 and seats[l] == 0:
                    res = max(res, r)
            if r == len(seats) - 1 and seats[r] == 0:
                res = max(res, len(seats) - 1 - l)
            if seats[r] == 1:
                res = max(res, (r - l) // 2)
                l = r
        return res
