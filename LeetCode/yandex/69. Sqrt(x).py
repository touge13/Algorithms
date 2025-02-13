class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        l = 1
        r = x
        res = 0
        while l <= r:
            mid = (l + r) // 2
            if mid ** 2 == x:
                return mid
            elif mid ** 2 > x:
                r = mid - 1
            else:
                res = mid 
                l = mid + 1
        return res
