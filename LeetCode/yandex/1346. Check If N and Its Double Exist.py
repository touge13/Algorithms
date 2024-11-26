class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        d = {}
        for n in arr:
            if (n / 2 in d) or (n * 2 in d):
                return True
            else:
                d[n] = 1
        return False
