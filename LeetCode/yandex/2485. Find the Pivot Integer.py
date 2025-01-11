class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        prefSum = {}
        s = 0
        for i in range(1, n + 1):
            s += i
            prefSum[i] = s
        for p in range(2, n + 1):
            if prefSum[n] - prefSum[p - 1] == prefSum[p]:
                return p
        return -1
