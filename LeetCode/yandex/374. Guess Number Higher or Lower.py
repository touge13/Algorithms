# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 0
        r = n
        while l <= r:
            mid = (l + r) // 2
            flag = guess(mid)
            if flag == 0:
                return mid
            elif flag == -1:
                r = mid - 1
            elif flag == 1:
                l = mid + 1
