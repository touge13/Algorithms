class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        res = 0
        l = 0
        for r in range(len(seats)):
            if r == len(seats) - 1 and seats[r] == 0:
                r += len(seats) - l # если в конце идут нули, то отодвинем r направо, чтобы компенсировать деление на 2 
                return max(res, (r - l) // 2)
            if seats[r] == 1:
                if l == 0 and seats[l] == 0:
                    l -= r # если сначала идут нули, то отодвинем l влево, чтобы компенсировать деление на 2 
                res = max(res, (r - l) // 2)
                l = r 
        return res
